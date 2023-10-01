import gradio as gr
from rembg import remove
from PIL import Image
import io
import numpy as np
import os

# Function to detect and save faces from an image
def run(input_image):#input_image, margin_ratio):
    try:
        return remove(Image.open(input_image))

    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Background Remover")
    
    with gr.Row():
        input_image = gr.Image(type="filepath", label="Input Image")
        output_image = gr.Image(label="Output Image")

    with gr.Column():
        margin_ratio=gr.Slider(0, 1, value=0, step=0.01, label='Cropping Margin Ratio')
        button=gr.Button("Proceed", variant="primary")

    button.click(fn=run,
                 inputs=input_image,
                 outputs=output_image)

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
