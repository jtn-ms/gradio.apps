import gradio as gr
import numpy as np
from moviepy.editor import *
import os

def clip(video,start_time,end_time):
    try:
        video_clip = VideoFileClip(video)
        if start_time != end_time:
            video_clip = video_clip.subclip(start_time, end_time)
        audio_clip = video_clip.audio
        
        output_audio_file = 'output.wav'
        if os.path.exists(os.path.abspath(output_audio_file)): os.remove(output_audio_file)
        audio_clip.write_audiofile(output_audio_file)

        return output_audio_file
    
    except Exception as e:
        return str(e)

demo = gr.Interface(
    clip,
    inputs=[
        gr.Video(label="Original video"),
        gr.Number(label='Start Time (seconds)', default=0, min=0),
        gr.Number(label='End Time (seconds)', default=0, min=0),
    ],
    outputs="audio")

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)