import gradio as gr
import face_recognition
from PIL import Image
import io
import numpy as np

# Function to calculate face similarity
def calculate_similarity(image1, image2):
    try:
        # Load and encode the face images
        image1 = face_recognition.load_image_file(image1)
        image2 = face_recognition.load_image_file(image2)

        encoding1 = face_recognition.face_encodings(image1)
        encoding2 = face_recognition.face_encodings(image2)

        if not encoding1 or not encoding2:
            return "Error: No faces detected in one or both images."

        # Calculate the face similarity score
        face_distance = face_recognition.face_distance([encoding1[0]], encoding2[0])
        similarity_score = 1 - face_distance[0]

        return similarity_score

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the Gradio interface
# iface = gr.Interface(
#     fn=calculate_similarity,
#     inputs=[gr.Image(label="Image 1"), gr.Image(label="Image 2")],
#     outputs=gr.Text(label="Similarity Score"),
#     title="Face Similarity Calculator",
#     description="Upload two face images to calculate their similarity.",
#     live=True,
# )

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Face Similarity")
    
    with gr.Column():
        button=gr.Button("Calc", variant="primary")

    button.click(fn=calculate_similarity,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=[gr.Image(type="filepath",label="Image 1"), gr.Image(type="filepath",label="Image 2")],
                 outputs=gr.Text(label="Similarity Score"))

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
