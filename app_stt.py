import gradio as gr
import speech_recognition as sr

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

# Function to perform speech-to-text conversion
def speech_to_text(audio):
    try:
        with sr.AudioFile(audio) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {str(e)}"

# Define the Gradio interface
iface = gr.Interface(
    fn=speech_to_text,
    inputs="audio",
    outputs="text",
    title="Speech-to-Text (STT) Demo",
    description="Upload an audio file, and the app will convert it to text.",
)

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
