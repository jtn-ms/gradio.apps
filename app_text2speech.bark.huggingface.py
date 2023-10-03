import gradio as gr
from scipy.io.wavfile import write as write_wav

# download and load all models
from transformers import AutoProcessor, AutoModel


processor = AutoProcessor.from_pretrained("suno/bark-small")
model = AutoModel.from_pretrained("suno/bark-small")

output_filepath = '/tmp/example_TTS.bark.small.wav'

# Function to perform text-to-speech conversion
def text_to_speech(text_prompt):
    try:
        # generate audio from text
        # text_prompt = """
        #     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
        #     But I also have other interests such as playing tic tac toe.
        # """
        inputs = processor(
            text=[text_prompt],
            return_tensors="pt",
        )
        speech_values = model.generate(**inputs, do_sample=True)
        sampling_rate = model.generation_config.sample_rate
        write_wav(output_filepath, rate=sampling_rate, data=speech_values.cpu().numpy().squeeze())
        return output_filepath
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