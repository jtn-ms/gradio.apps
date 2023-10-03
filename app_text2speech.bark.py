import gradio as gr
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# download and load all models
preload_models()

# Function to perform text-to-speech conversion
def text_to_speech(text_prompt):
    try:
        # generate audio from text
        # text_prompt = """
        #     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
        #     But I also have other interests such as playing tic tac toe.
        # """
        audio_array = generate_audio(text_prompt)

        # save audio to disk
        write_wav('/tmp/example_TTS.bark.wav', SAMPLE_RATE, audio_array)

        return '/tmp/example_TTS.bark.wav'
    except Exception as e:
        print(str(e))
        return None

# Define the Gradio interface
demo = gr.Interface(
    fn=text_to_speech,
    inputs="text",
    outputs="audio",
    title="Text-to-Speech (TTS) Demo",
    description="Enter text, and the app will convert it to audio.",
)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)