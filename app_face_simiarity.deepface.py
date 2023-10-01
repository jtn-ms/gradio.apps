import gradio as gr
from deepface import DeepFace
from PIL import Image
import io
import numpy as np

# Function to calculate face similarity
def calculate_similarity(image1, image2):
    try:
        return DeepFace.verify(img1_path = image1, img2_path = image2)

    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# DeepFace Similarity")
    with gr.Row():
        inputs=[gr.Image(type="filepath",label="Image 1"), gr.Image(type="filepath",label="Image 2")]
    with gr.Column():
        output=gr.Text(label="Similarity Score")
        button=gr.Button("Calc", variant="primary")

    button.click(fn=calculate_similarity,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=inputs,
                 outputs=output)

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
