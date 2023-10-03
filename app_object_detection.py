import gradio as gr
from PIL import Image
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

# Function to detect objects
def detect(input_image):#input_image, margin_ratio):
    try:
        image = Image.open(input_image)
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        # convert outputs (bounding boxes and class logits) to COCO API
        # let's only keep detections with score > 0.9
        target_sizes = torch.tensor([image.size[::-1]])
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

        results_str = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            results_str.append(
                    f"Detected {model.config.id2label[label.item()]} with confidence "
                    f"{round(score.item(), 3)} at location {box}"
            )

        return results_str

    except Exception as e:
        return f"An error occurred: {str(e)}"

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Object Detection")
    
    with gr.Column():
        input_image = gr.Image(type="filepath", label="Image")
        button=gr.Button("Detect", variant="primary")

    button.click(fn=detect,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=[input_image],
                 outputs=gr.Text(label="Result"))

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)
