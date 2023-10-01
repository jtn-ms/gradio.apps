import gradio as gr
# import whisper
from transformers import pipeline
import numpy as np

# model = whisper.load_model("base")
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

def transcribe(audio):
    try:
        sr, y = audio
        y = y.mean(axis=1) # # Convert the audio to mono by taking the mean across channels (axis 1)
        y = y.astype(np.float32)
        y /= np.max(np.abs(y))

        # return model.transcribe(y)
        return transcriber({"sampling_rate": sr, "raw": y})["text"]

    except Exception as e:
        return str(e)

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Audio Transcription")

    with gr.Row():
        inputs=gr.Audio()
        outputs=gr.Text(label="Result")

    with gr.Column():
        button=gr.Button("Detect", variant="primary")

    button.click(fn=transcribe,
                 inputs=inputs,
                 outputs=outputs)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)