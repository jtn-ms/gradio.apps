import gradio as gr
from transformers import pipeline
import numpy as np

# https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&sort=likes&search=en
# whisper model is the best
models = {
    "en-whisper-base": "openai/whisper-base.en",
    "en-whisper-small": "openai/whisper-small.en",
    "zh-whisper-small": "xmzhu/whisper-small-zh",
    "ko-whisper-small":"SungBeom/whisper-small-ko", 
    "en-wav2vec2-large-xlsr-53":"jonatasgrosman/wav2vec2-large-xlsr-53-english",
    "zh-wav2vec2-large-xlsr-53": "jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn",
    "ko-wav2vec2-large-xlsr": "kresnik/wav2vec2-large-xlsr-korean",
}

langs = list(models.keys())
current_lang = langs[0]
pipe = None
concatenated_result=""
chunk_cnt = 0
chunk_size = 20
sr = 0 # sample rate

def change_pipe(lang):
    global pipe
    pipe = pipeline("automatic-speech-recognition", model=models[lang])

change_pipe(current_lang)

def transcribe(lang, stream, new_chunk):
    
    global current_lang
    global concatenated_result
    global chunk_cnt
    global chunk_size
    global sr

    chunk_cnt += 1
    # print(chunk_cnt)

    # change model
    if lang and current_lang != lang:
        change_pipe(lang)
        current_lang=lang

    if 1:
        if not new_chunk and not stream: return stream, concatenated_result
        if not new_chunk and stream:
            concatenated_result += pipe({"sampling_rate": sr, "raw": stream})["text"]
            stream = None
            chunk_cnt = 0
            return stream, concatenated_result
    else:
        if not new_chunk: return stream, "No streaming...\n"+concatenated_result

    sr, y = new_chunk
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    stream = np.concatenate([stream, y]) if stream is not None else y

    if chunk_cnt >= chunk_size:
        concatenated_result += pipe({"sampling_rate": sr, "raw": stream})["text"]
        stream = None
        chunk_cnt = 0

    return stream, concatenated_result

demo = gr.Interface(
    transcribe,
    [gr.Dropdown(langs,label="Language", info="Choose Language"),"state", gr.Audio(source="microphone", streaming=True)],
    ["state", gr.Textbox(label="Output")],
    # allow_flagging='never',
    # show_progress=False,
    live=True,
)

# demo.dependencies[0]["show_progress"] = False  # the hack

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)