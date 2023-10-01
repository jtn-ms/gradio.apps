import gradio as gr
from PIL import Image
import io
import numpy as np

# https://huggingface.co/nlpconnect/vit-gpt2-image-captioning
# from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
# import torch

# model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# max_length = 16
# num_beams = 4
# gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

# def predict_step(image_paths):
#   images = []
#   for image_path in image_paths:
#     i_image = Image.open(image_path)
#     if i_image.mode != "RGB":
#       i_image = i_image.convert(mode="RGB")

#     images.append(i_image)

#   pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
#   pixel_values = pixel_values.to(device)

#   output_ids = model.generate(pixel_values, **gen_kwargs)

#   preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
#   preds = [pred.strip() for pred in preds]
#   return preds

# # Function to generate a caption for an image
# def run(img_path):
#     try:
#         return predict_step[img_path]
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

from transformers import pipeline

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

image_to_text("https://ankur3107.github.io/assets/images/image-captioning-example.png")

# Function to generate a caption for an image
def run(img_path):
    try:
        return image_to_text(img_path)[0]['generated_text']
    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Image Captioning")
    with gr.Row():
        with gr.Column():
            inputs=gr.Image(type="filepath",label="Input Image")
            button=gr.Button("Proceed", variant="primary")
        # output=gr.Text(label="explanation")

    button.click(fn=run,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=inputs,
                 outputs=gr.Text(label="explanation"))

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)