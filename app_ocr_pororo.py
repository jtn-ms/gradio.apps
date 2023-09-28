import gradio as gr
from PIL import Image
import io
import numpy as np
import os

from pororo import Pororo
from main import PororoOcr
ocr = PororoOcr()

# Function to detect and save faces from an image
def run_ocr(input_image,lang="korean"):#input_image, margin_ratio):
    try:
        ocr.change_model(lang)
        return ocr.run_ocr(input_image)
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# pororoOCR")
    
    with gr.Column():
        input_image = gr.Image(type="filepath", label="Image")
        lang=gr.Dropdown(ocr.get_available_langs(),label="Language", info="Select Language Model")
        button=gr.Button("OCR", variant="primary")

    button.click(fn=run_ocr,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=[input_image,lang],
                 outputs=gr.Text(label="Result"))

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
