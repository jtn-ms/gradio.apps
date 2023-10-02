import gradio as gr
from transformers import pipeline
from PIL import Image
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionUpscalePipeline
import torch

# load model and scheduler
model_id = "stabilityai/stable-diffusion-x4-upscaler"
pipeline = StableDiffusionUpscalePipeline.from_pretrained(model_id, torch_dtype=torch.float32)
# pipeline = pipeline.to("cuda")

# Function to upscale
def upscale(img, prompt):
    try:
        return pipeline(prompt=prompt, image=img).images[0]
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Upscale Image")
    with gr.Row():
        with gr.Column():
            inputs=[gr.Image(type="filepath",label="Original"),gr.Text(label="What is your prompt?")]
            button=gr.Button("Proceed", variant="primary")
        output=gr.Image(label="Result")

    button.click(fn=upscale,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=inputs,
                 outputs=output)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)