import gradio as gr
from transformers import pipeline
from PIL import Image
import io
import numpy as np

vqa = pipeline(model="impira/layoutlm-document-qa")

# Function to calculate face similarity
def calculate_similarity(img, query):
    try:
        return vqa(img, query)
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Answer your question about Image")
    with gr.Row():
        with gr.Column():
            inputs=[gr.Image(type="filepath",label="Image 1"),gr.Text(label="What is your question?")]
            button=gr.Button("Proceed", variant="primary")
        output=gr.Text(label="Answer")

    button.click(fn=calculate_similarity,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=inputs,
                 outputs=output)

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)