import gradio as gr
from PIL import Image
import io
import numpy as np
import os
import cv2

from transformers import SegformerImageProcessor, AutoModelForSemanticSegmentation
from PIL import Image
import matplotlib.pyplot as plt
import torch.nn as nn
import torch


processor = SegformerImageProcessor.from_pretrained("mattmdjaga/segformer_b2_clothes")
model = AutoModelForSemanticSegmentation.from_pretrained("mattmdjaga/segformer_b2_clothes")

# Function to detect and save faces from an image
def run(input_image):#input_image, margin_ratio):
    try:
        image = Image.open(input_image)
        # Convert the PIL image to a NumPy array (OpenCV image)
        cv_image = np.array(image)
        # If needed, you can convert from BGR to RGB (OpenCV uses BGR by default)
        cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits.cpu()
        upsampled_logits = nn.functional.interpolate(
            logits,
            size=image.size[::-1],
            mode="bilinear",
            align_corners=False,
        )
        pred_seg = upsampled_logits.argmax(dim=1)[0]
        # Assuming you have a torch tensor for pred_seg (shape: [height, width])
        # Convert it to a binary mask (0 for background, 1 for foreground)
        threshold = 0.5  # Adjust this threshold as needed
        pred_mask = (pred_seg > threshold).to(torch.uint8).cpu().numpy()

        # Create a transparent background image with the same dimensions as the original image
        transparent_background = np.zeros_like(cv_image_rgb, dtype=np.uint8)
        # Copy the foreground object from the original image to the transparent background
        transparent_background[pred_mask == 1] = cv_image_rgb[pred_mask == 1]
        # cv2.imwrite('/tmp/bg.imgseg.result_image.png', transparent_background)
        return transparent_background#'/tmp/bg.imgseg.result_image.png'

    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Background Remover")
    
    with gr.Row():
        input_image = gr.Image(type="filepath", label="Input Image")
        output_image = gr.Image(label="Output Image")

    with gr.Column():
        button=gr.Button("Proceed", variant="primary")

    button.click(fn=run,
                 inputs=input_image,
                 outputs=output_image)

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
