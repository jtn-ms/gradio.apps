import gradio as gr
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

# Function to clip the video and convert to GIF
def clip_and_convert(video_file, start_time, end_time):
    # Create a subclip using MoviePy
    input_video = VideoFileClip(video_file)
    subclip = input_video.subclip(start_time, end_time)

    # Define output file paths
    output_video_path = 'output.mp4'
    output_gif_path = 'output.gif'

    # Write the subclip as a video file
    subclip.write_videofile(output_video_path, codec='libx264')

    # Convert the video to GIF using MoviePy
    input_video = VideoFileClip(output_video_path)
    input_video.write_gif(output_gif_path)

    # Remove the temporary video file
    os.remove(output_video_path)

    return output_gif_path

# Create the Gradio interface
demo = gr.Interface(
    fn=clip_and_convert,
    inputs=[
        gr.Video(label="Select Video File",format="mp4"),
        gr.Number(label='Start Time (seconds)', default=0, min=0),
        gr.Number(label='End Time (seconds)', default=10, min=0),
    ],
    outputs=gr.Image(label='Clipped and Converted GIF'),
)

# with gr.Blocks() as demo:
#     with gr.Row():
#         gr.Markdown("# Video to Giff")

#     with gr.Column():
#         button=gr.Button("Convert", variant="primary")

#     button.click(fn=clip_and_convert,
#                 inputs=[
#                     gr.Video(label="Select Video File",format="mp4"),
#                     gr.Number(label='Start Time (seconds)', default=0, min=0),
#                     gr.Number(label='End Time (seconds)', default=10, min=0),
#                 ],
#                 outputs=gr.Image(label='Clipped and Converted GIF'))

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(debug=True,server_name="0.0.0.0",server_port=8080)