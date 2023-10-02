import gradio as gr
from transformers import pipeline
from PIL import Image
import io
import numpy as np
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float32)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# pipe.enable_model_cpu_offload()

# Function to generate Video from text
def txt2vid(prompt,num_frames):
    try:
        video_frames = pipe(prompt, num_inference_steps=40, height=320, width=576, num_frames=num_frames).frames
        video_path = export_to_video(video_frames)
        return video_path
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Text-to-Video")
    with gr.Row():
        with gr.Column():
            inputs=[gr.Text(label="Illustrate what you have in your mind."),gr.Number(label="Number of Frames")]
            button=gr.Button("Proceed", variant="primary")
        output=gr.Video(label="Output Video")

    button.click(fn=txt2vid,
                 inputs=inputs,
                 outputs=output)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)