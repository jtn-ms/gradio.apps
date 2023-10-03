import gradio as gr
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/lang-id-commonlanguage_ecapa", savedir="pretrained_models/lang-id-commonlanguage_ecapa")


# Function to perform speech-to-text conversion
def speech_to_text(audio):
    try:
        out_prob, score, index, text_lab = classifier.classify_file(audio)
        return text_lab
    except Exception as e:
        return f"Could not request results; {str(e)}"

# Define the Gradio interface
demo = gr.Interface(
    fn=speech_to_text,
    inputs="audio",
    outputs="text",
    title="Language Detection From Speech",
    description="Upload an audio file, and the app will tell the language.",
)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)
