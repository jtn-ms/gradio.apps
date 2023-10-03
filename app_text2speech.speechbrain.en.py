import gradio as gr
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech", savedir="/tmp/tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="/tmp/tmpdir_vocoder")

# Function to perform text-to-speech conversion
def text_to_speech(text):
    try:
        # Running the TTS
        mel_output, mel_length, alignment = tacotron2.encode_text(text)

        # Running Vocoder (spectrogram-to-waveform)
        waveforms = hifi_gan.decode_batch(mel_output)

        # Save the waverform
        torchaudio.save('/tmp/example_TTS.en.wav',waveforms.squeeze(1), 22050)

        return '/tmp/example_TTS.wav'
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