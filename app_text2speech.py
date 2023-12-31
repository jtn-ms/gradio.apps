import gradio as gr
from gtts import gTTS
import tempfile
import os

langs = ["en", "zh", "ko","jp","fr","ru"]

# Function to perform text-to-speech conversion
def text_to_speech(lang,text):
    tts = gTTS(text=text, lang=lang)
    # Save the TTS output as an audio file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_audio:
        tts.save(tmp_audio.name)
    return tmp_audio.name

# Function to perform speech-to-text conversion (not supported by gTTS, placeholder)
def speech_to_text(audio):
    # You can implement a proper speech-to-text conversion here (e.g., using a library like SpeechRecognition)
    return "Speech-to-text conversion not implemented."

# Define the Gradio interface
demo = gr.Interface(
    fn=text_to_speech,
    inputs=[gr.Dropdown(langs,label="Source", info="Choose Language"),"text"],
    outputs="audio",
    title="Text-to-Speech (TTS) Demo",
    description="Enter text, and the app will convert it to audio.",
)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)