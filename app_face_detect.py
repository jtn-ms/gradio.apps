import gradio as gr
import face_recognition
from PIL import Image
import io
import numpy as np
import os

# Function to detect and save faces from an image
def detect_and_save_faces(*var):#input_image, margin_ratio):
    input_image=var[0]
    margin_ratio=var[1]
    try:
        # Load the input image
        image = face_recognition.load_image_file(input_image)
        height, width = image.shape[:2]
        # print(width,height)

        # Detect faces in the image
        face_locations = face_recognition.face_locations(image)

        if not face_locations:
            return "No faces detected in the image."

        # Create a directory to save the faces
        # os.makedirs("detected_faces", exist_ok=True)

        # Save each detected face as a separate image
        saved_face_paths = []
        faces = []
        margin_ratio_value = margin_ratio
        for i, face_location in enumerate(face_locations):
            top, right, bottom, left = face_location
            if margin_ratio_value != 0:
                w,h=right-left,bottom-top
                top, bottom = top - int(h*margin_ratio_value), bottom+int(h*margin_ratio_value)
                left,right = left - int(w*margin_ratio_value), right+int(w*margin_ratio_value)
                if top < 0: top = 0
                if left < 0: left = 0
                if bottom > height-1: bottom = height -1
                if right > width - 1: right=width -1

            face_image = image[top:bottom, left:right]
            face_image = Image.fromarray(face_image)

            # Save the face image
            # face_path = f"detected_faces/face_{i}.jpg"
            # face_image.save(face_path)
            # saved_face_paths.append(face_path)
            faces.append(face_image)
        # Generate output components dynamically based on the length of the array
        return faces+[Image.new("RGB", (10, 10), (255, 255, 255))]*(max_num_faces-len(faces))#[gr.Image(label=f"Detected Face{i}",value=faces[i]) for i in range(len(faces))]

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the Gradio interface
# iface = gr.Interface(
#     fn=detect_and_save_faces,
#     inputs=gr.Image(type="filepath", label="Image"),
#     outputs=[gr.Image(label="Detected Face",type="filepath")],
#     title="Face Detection and Download",
#     description="Upload an image to detect faces and download the detected faces.",
#     live=True,
# )

max_num_faces = 20

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Face Detection")
    
    with gr.Row():
        input_image = gr.Image(type="filepath", label="Image")

        faces = []
        for i in range(0,max_num_faces):
            with gr.Tab(f"Face #{i+1}"):
                with gr.Row():
                    face = gr.Image(label=f"Face {i}").style(height=200)
                    faces.append(face)

    with gr.Column():
        margin_ratio=gr.Slider(0, 1, value=0, step=0.01, label='Cropping Margin Ratio')
        button=gr.Button("Detect", variant="primary")

    button.click(fn=detect_and_save_faces,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=[input_image,margin_ratio],
                 outputs=faces)

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
