import gradio as gr
from transformers import pipeline
from PIL import Image
import io
import numpy as np

import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_XL", torch_dtype=torch.float32)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# pipe.enable_model_cpu_offload()
pipe.enable_vae_slicing()
# pipe.enable_model_cpu_offload()

from moviepy.editor import *

# Function to generate Video from text
def vid2vid(prompt,video,num_frames):
    try:
        video_clip = VideoFileClip(video)
        # # getting only first 5 seconds
        # video_clip = video_clip.subclip(0, 5)
        
        # iterating frames
        frames = video_clip.iter_frames()

        video = [Image.fromarray(frame).resize((1024, 576)) for frame in frames]

        frames = pipe(prompt, video=video, strength=0.6).frames

        return export_to_video(frames)
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Text-to-Video")
    with gr.Row():
        with gr.Column():
            inputs=[gr.Text(label="Prompt used for video").gr.Video(label="Original video")]
            button=gr.Button("Proceed", variant="primary")
        output=gr.Video(label="Output Video")

    button.click(fn=vid2vid,
                 inputs=inputs,
                 outputs=output)

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)