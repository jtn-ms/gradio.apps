import gradio as gr
from transformers import pipeline
import numpy as np
from moviepy.editor import *

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

def transcribe(video,start_time,end_time):
    try:
        video_clip = VideoFileClip(video)
        if start_time != end_time:
            video_clip = video_clip.subclip(start_time, end_time)
        audio_clip = video_clip.audio

        sr, y = audio_clip.fps,audio_clip.to_soundarray()
        y = y.mean(axis=1) # # Convert the audio to mono by taking the mean across channels (axis 1)
        y = y.astype(np.float32)
        y /= np.max(np.abs(y))

        return transcriber({"sampling_rate": sr, "raw": y})["text"]
    
    except Exception as e:
        return str(e)

demo = gr.Interface(
    transcribe,
    inputs=[
        gr.Video(label="Original video"),
        gr.Number(label='Start Time (seconds)', default=0, min=0),
        gr.Number(label='End Time (seconds)', default=10, min=0),
    ],
    outputs="text")

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)