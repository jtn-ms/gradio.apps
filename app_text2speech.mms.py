import gradio as gr
import tempfile
import os
import scipy

from transformers import VitsModel, AutoTokenizer
import torch

models = ["facebook/mms-tts-eng","facebook/mms-tts-kor"]
cur_mid = models[0]

model = None
tokenizer=None

def change_pipe(model_id):
    global model
    global tokenizer
    global cur_mid
    cur_mid = model_id
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = VitsModel.from_pretrained(model_id)

change_pipe(cur_mid)

# Function to perform text-to-speech conversion
def text_to_speech(model_id,text):
    try:
        global model
        global tokenizer
        global cur_mid

        if model_id and model_id != cur_mid: change_pipe(model_id)

        inputs = tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            output = model(**inputs).waveform
            scipy.io.wavfile.write("/tmp/techno.wav", rate=model.config.sampling_rate, data=output)
        return output
    except Exception as e:
        print(str(e))
        return None

# Define the Gradio interface
demo = gr.Interface(
    fn=text_to_speech,
    inputs=[gr.Dropdown(models,label="Model", info="Choose Model"),"text"],
    outputs="audio",
    title="Text-to-Speech (TTS) Demo",
    description="Enter text, and the app will convert it to audio.",
)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)