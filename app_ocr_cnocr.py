import gradio as gr
from PIL import Image
import io
import numpy as np
import os

# https://github.com/breezedeus/CnOCR
from cnocr import CnOcr
ocr = CnOcr() 
# Function to detect and save faces from an image
def run_ocr(input_image):#input_image, margin_ratio):
    try:
        results = ocr.ocr(input_image)
        return " ".join([result['text'] for result in results])
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# CnOcr")
    
    with gr.Column():
        input_image = gr.Image(type="filepath", label="Image")
        button=gr.Button("OCR", variant="primary")

    button.click(fn=run_ocr,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=[input_image],
                 outputs=gr.Text(label="Result"))

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)
