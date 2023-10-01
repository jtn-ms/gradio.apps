import cv2
import numpy as np
import gradio as gr

import os
import copy
import argparse
import insightface
import onnxruntime
from PIL import Image
from typing import List, Union, Dict, Set, Tuple


def getFaceSwapModel(model_path: str):
    model = insightface.model_zoo.get_model(model_path)
    return model


def getFaceAnalyser(model_path: str, providers,
                    det_size=(320, 320)):
    face_analyser = insightface.app.FaceAnalysis(name="buffalo_l", root="./checkpoints", providers=providers)
    face_analyser.prepare(ctx_id=0, det_size=det_size)
    return face_analyser


def get_one_face(face_analyser,
                 frame:np.ndarray):
    face = face_analyser.get(frame)
    try:
        return min(face, key=lambda x: x.bbox[0])
    except ValueError:
        return None

    
def get_many_faces(face_analyser,
                   frame:np.ndarray):
    """
    get faces from left to right by order
    """
    try:
        face = face_analyser.get(frame)
        return sorted(face, key=lambda x: x.bbox[0])
    except IndexError:
        return None


def swap_face(face_swapper,
              source_faces,
              target_faces,
              source_index,
              target_index,
              temp_frame):
    """
    paste source_face on target image
    """
    source_face = source_faces[source_index]
    target_face = target_faces[target_index]

    return face_swapper.get(temp_frame, target_face, source_face, paste_back=True)
 

from restoration import *

def run(*var):
    target_img=var[0]
    source_indexes=var[1]
    target_indexes=var[2]
    num_source_images=var[3]
    enableface_restore=var[4]
    background_enhance=var[5]
    face_upsample=var[6]
    upscale=var[7]
    codeformer_fidelity=var[8]
    source_imgs=var[9:]

    # load machine default available providers
    providers = onnxruntime.get_available_providers()

    model = "./checkpoints/inswapper_128.onnx"
    # load face_analyser
    face_analyser = getFaceAnalyser(model, providers)
    # load face_swapper
    model_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), model)
    face_swapper = getFaceSwapModel(model_path)
    
    # read target image
    target_img = cv2.cvtColor(np.array(target_img), cv2.COLOR_RGB2BGR)
    print(type(target_img))
    
    # detect faces that will be replaced in the target image
    target_faces = get_many_faces(face_analyser, target_img)
    num_target_faces = len(target_faces)

    if target_faces is not None:
        temp_frame = copy.deepcopy(target_img)
        if isinstance(source_imgs, list) and num_source_images == num_target_faces:
            print("Replacing faces in target image from the left to the right by order")
            for i in range(num_target_faces):
                source_faces = get_many_faces(face_analyser, cv2.cvtColor(np.array(source_imgs[i]), cv2.COLOR_RGB2BGR))
                source_index = i
                target_index = i

                if source_faces is None:
                    raise Exception("No source faces found!")

                temp_frame = swap_face(
                    face_swapper,
                    source_faces,
                    target_faces,
                    source_index,
                    target_index,
                    temp_frame
                )
        elif num_source_images == 1:
            # detect source faces that will be replaced into the target image
            print(type(source_imgs[0]),source_imgs[0])
            source_faces = get_many_faces(face_analyser, cv2.cvtColor(np.array(source_imgs[0]), cv2.COLOR_RGB2BGR))
            num_source_faces = len(source_faces)
            print(f"Source faces: {num_source_faces}")
            print(f"Target faces: {num_target_faces}")

            if source_faces is None:
                raise Exception("No source faces found!")

            if target_indexes == "-1":
                if num_source_faces == 1:
                    print("Replacing all faces in target image with the same face from the source image")
                    num_iterations = num_target_faces
                elif num_source_faces < num_target_faces:
                    print("There are less faces in the source image than the target image, replacing as many as we can")
                    num_iterations = num_source_faces
                elif num_target_faces < num_source_faces:
                    print("There are less faces in the target image than the source image, replacing as many as we can")
                    num_iterations = num_target_faces
                else:
                    print("Replacing all faces in the target image with the faces from the source image")
                    num_iterations = num_target_faces

                for i in range(num_iterations):
                    source_index = 0 if num_source_faces == 1 else i
                    target_index = i

                    temp_frame = swap_face(
                        face_swapper,
                        source_faces,
                        target_faces,
                        source_index,
                        target_index,
                        temp_frame
                    )
            else:
                print("Replacing specific face(s) in the target image with specific face(s) from the source image")

                if source_indexes == "-1":
                    source_indexes = ','.join(map(lambda x: str(x), range(num_source_faces)))

                if target_indexes == "-1":
                    target_indexes = ','.join(map(lambda x: str(x), range(num_target_faces)))

                source_indexes = source_indexes.split(',')
                target_indexes = target_indexes.split(',')
                num_source_faces_to_swap = len(source_indexes)
                num_target_faces_to_swap = len(target_indexes)

                if num_source_faces_to_swap > num_source_faces:
                    raise Exception("Number of source indexes is greater than the number of faces in the source image")

                if num_target_faces_to_swap > num_target_faces:
                    raise Exception("Number of target indexes is greater than the number of faces in the target image")

                if num_source_faces_to_swap > num_target_faces_to_swap:
                    num_iterations = num_source_faces_to_swap
                else:
                    num_iterations = num_target_faces_to_swap

                if num_source_faces_to_swap == num_target_faces_to_swap:
                    for index in range(num_iterations):
                        source_index = int(source_indexes[index])
                        target_index = int(target_indexes[index])

                        if source_index > num_source_faces-1:
                            raise ValueError(f"Source index {source_index} is higher than the number of faces in the source image")

                        if target_index > num_target_faces-1:
                            raise ValueError(f"Target index {target_index} is higher than the number of faces in the target image")

                        temp_frame = swap_face(
                            face_swapper,
                            source_faces,
                            target_faces,
                            source_index,
                            target_index,
                            temp_frame
                        )
        else:
            raise Exception("Unsupported face configuration")
        result = temp_frame
    else:
        print("No target faces found!")
    
    result_image = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    # face restoration
    background_enhance = background_enhance if background_enhance is not None else True
    face_upsample = face_upsample if face_upsample is not None else True
    upscale = upscale if (upscale is not None and upscale > 0) else 2

    upscale = int(upscale) # convert type to int
    if upscale > 4: # avoid memory exceeded due to too large upscale
        upscale = 4 

    if enableface_restore:
        
        # make sure the ckpts downloaded successfully
        check_ckpts()
        
        # https://huggingface.co/spaces/sczhou/CodeFormer
        upsampler = set_realesrgan()
        device = torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")

        codeformer_net = ARCH_REGISTRY.get("CodeFormer")(dim_embd=512,
                                                         codebook_size=1024,
                                                         n_head=8,
                                                         n_layers=9,
                                                         connect_list=["32", "64", "128", "256"],
                                                        ).to(device)
        ckpt_path = "CodeFormer/CodeFormer/weights/CodeFormer/codeformer.pth"
        checkpoint = torch.load(ckpt_path)["params_ema"]
        codeformer_net.load_state_dict(checkpoint)
        codeformer_net.eval()
        
        result_image = cv2.cvtColor(np.array(result_image), cv2.COLOR_RGB2BGR)
        result_image = face_restoration(result_image, 
                                        background_enhance, 
                                        face_upsample, 
                                        upscale, 
                                        codeformer_fidelity,
                                        upsampler,
                                        codeformer_net,
                                        device)
        result_image = Image.fromarray(result_image)
    return result_image


def parse_args():
    parser = argparse.ArgumentParser(description="Face swap.")
    # parser.add_argument("--source_imgs", type=str, required=True, help="The path of source image, it can be multiple images, dir;dir2;dir3.")
    # parser.add_argument("--target_img", type=str, required=True, help="The path of target image.")
    # parser.add_argument("--output_img", type=str, required=False, default="result.png", help="The path and filename of output image.")
    # parser.add_argument("--source_indexes", type=str, required=False, default="-1", help="Comma separated list of the face indexes to use (left to right) in the source image, starting at 0 (-1 uses all faces in the source image")
    # parser.add_argument("--target_indexes", type=str, required=False, default="-1", help="Comma separated list of the face indexes to swap (left to right) in the target image, starting at 0 (-1 swaps all faces in the target image")
    parser.add_argument("--face_restore", action="store_true", help="The flag for face restoration.")
    parser.add_argument("--background_enhance", action="store_true", help="The flag for background enhancement.")
    parser.add_argument("--face_upsample", action="store_true", help="The flag for face upsample.")
    parser.add_argument("--upscale", type=int, default=1, help="The upscale value, up to 4.")
    parser.add_argument("--codeformer_fidelity", type=float, default=0.5, help="The codeformer fidelity.")
    args = parser.parse_args()
    return args
    
origin = []

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# Refacer")
    with gr.Column():
        source_indexes=gr.Textbox(value="-1",label="source indexes")
        dest_indexes=gr.Textbox(value="-1",label="dest indexes")
        num_of_sources=gr.Number(label="Number of Images",value=1)
        enable_face_restore=gr.Checkbox(value=True, label="Face_Restore")
        bkg_enhance=gr.Checkbox(value=True, label="Background_Enhance")
        face_upsample=gr.Checkbox(value=True, label="Face_Upsample")
        scaler=gr.Number(value=1, label="Rescaling_Factor (up to 4)")
        fidelity=gr.Slider(0, 1, value=0.5, step=0.01, label='Codeformer_Fidelity (0 for better quality, 1 for better identity)')
        
    with gr.Row():
        for i in range(0,int(num_of_sources.value)):
            with gr.Tab(f"Face #{i+1}"):
                with gr.Row():
                    origin.append(gr.Image(label="Face to replace"))
        targetImg=gr.Image(label="Target Image")
    # num_of_sources = num_of_sources if (num_of_sources is not None and int(num_of_sources.value) > 0) else 1
    # num_of_sources = 2

                # destination=gr.Image(label="Destination face")
            # with gr.Row():
            #     gr.Checkbox(value=True, label="Face_Restore"),
            #     gr.Checkbox(value=True, label="Background_Enhance")
            #     gr.Checkbox(value=True, label="Face_Upsample")
            #     gr.Number(value=2, label="Rescaling_Factor (up to 4)")
            #     gr.Slider(0, 1, value=0.5, step=0.01, label='Codeformer_Fidelity (0 for better quality, 1 for better identity)')
    
    with gr.Column():
        destImg=gr.Image(label="Result")
        button=gr.Button("Reface", variant="primary")

    input_var=[targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity]+origin
    button.click(fn=run,
                #  inputs=[origin,targetImg,source_indexes,dest_indexes,num_of_sources,enable_face_restore,bkg_enhance,face_upsample,scaler,fidelity],
                 inputs=input_var,
                 outputs=destImg)


# Define the Gradio interface with dynamic inputs
# iface = gr.Interface(
#     fn=run,
#     inputs=[
#         gr.Image(label="Destination Image"),
#         gr.Textbox(value="-1",label="source indexes"),
#         gr.Textbox(value="-1",label="dest indexes"),
#         gr.Number(label="Number of Images", default=1, min=1, max=5),
#         *[gr.Image(type="filepath", label=f"Image {i + 1}") for i in range(1)],
#     ],
#     outputs=gr.Image(type="numpy", label="Output").style(height='auto'),
#     title="Image Merger",
#     description="Upload two or more images to merge them into a single large image.",
#     live=True,
# )


# Launch the Gradio web service
if __name__ == "__main__":
    args = parse_args()
    iface.launch(debug=True,server_name="0.0.0.0",server_port=8080)