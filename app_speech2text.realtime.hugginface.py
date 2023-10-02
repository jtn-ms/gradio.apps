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

def change_pipe(lang):
    global pipe
    pipe = pipeline("automatic-speech-recognition", model=models[lang])

change_pipe(current_lang)

def transcribe(lang, stream, new_chunk):
    # change model
    global current_lang
    if lang and current_lang != lang:
        change_pipe(lang)
        current_lang=lang

    sr, y = new_chunk
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    if stream is not None:
        stream = np.concatenate([stream, y])
    else:
        stream = y
    return stream, pipe({"sampling_rate": sr, "raw": stream})["text"]

# with gr.Blocks() as demo:
#     with gr.Row():
#         lang=gr.Dropdown(langs,label="Language", info="Choose Language")
#         button=gr.Button("Recognition", variant="primary")
#     lang.change(fn=change_pipe,inputs=lang)
#     button.click(fn=transcribe,
#                 inputs=["state", gr.Audio(source="microphone", streaming=True)],
#                 outputs=["state", "text"],
#     )

# # https://github.com/gradio-app/gradio/issues/2093
# with gr.Blocks() as demo:
#     lang=gr.Dropdown(langs,label="Language", info="Choose Language")
#     mic = gr.Audio(source="microphone")
#     text = gr.Textbox()
#     mic.stream(transcribe, [lang,"state",mic], ["state",text])

demo = gr.Interface(
    transcribe,
    [gr.Dropdown(langs,label="Language", info="Choose Language"),"state", gr.Audio(source="microphone", streaming=True)],
    ["state", gr.Textbox(label="Output")],
    allow_flagging='never',
    show_progress=False,
    live=True,
)

# demo.dependencies[0]["show_progress"] = False  # the hack

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)