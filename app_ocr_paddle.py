#-*- coding:utf-8 -*-
import gradio as gr
# import io
import cv2
import numpy as np
import platform
from PIL import ImageFont, ImageDraw, Image
from matplotlib import pyplot as plt


def plt_imshow(title='image', img=None, figsize=(8, 5)):
    plt.figure(figsize=figsize)

    if type(img) is str:
        img = cv2.imread(img)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()


def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
    if type(image) == np.ndarray:
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(color_coverted)

    font = 'DejaVuSans.ttf'
    if platform.system() == 'Darwin':
        font = 'AppleGothic.ttf'
    elif platform.system() == 'Windows':
        font = 'malgun.ttf'

    image_font = ImageFont.truetype(font, font_size)
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text, fill=color, font=image_font)

    numpy_image = np.array(image)
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    return opencv_image

from paddleocr import PaddleOCR
from paddleocr.paddleocr import MODEL_URLS

# https://github.com/yunwoong7/korean_ocr_using_paddleOCR
class MyPaddleOCR:
    def __init__(self, lang: str = "ch", **kwargs):
        self.lang = lang
        self._ocr = PaddleOCR(lang="ch")
        self.img_path = None
        self.ocr_result = {}
    
    def get_available_langs(self):
        langs_info = []

        for idx, model_name in enumerate(list(MODEL_URLS['OCR'].keys())):
            for lang in list(MODEL_URLS['OCR'][model_name]['rec'].keys()):
                if lang not in langs_info:
                    langs_info.append(lang)
        
        # print('Available Language : {}'.format(langs_info))
        return langs_info
        
    def get_available_models(self):
        model_info = {}

        for idx, model_name in enumerate(list(MODEL_URLS['OCR'].keys())):
            model_info[model_name] = list(MODEL_URLS['OCR'][model_name]['rec'].keys())
            print('#{} Model Vesion : [{}] - Language : {}'.format(idx+1, model_name, list(MODEL_URLS['OCR'][model_name]['rec'].keys())))
        
    def get_ocr_result(self):
        return self.ocr_result

    def get_img_path(self):
        return self.img_path

    def change_model(self,lang):
        if lang == self.lang: return
        self._ocr = PaddleOCR(lang=lang)
    # def show_img(self):
    #     plt_imshow(img=self.img_path)
        
    def run_ocr(self, img_path: str, debug: bool = False):
        self.img_path = img_path
        ocr_text = []
        result = self._ocr.ocr(img_path, cls=False)
        self.ocr_result = result[0]

        if self.ocr_result:
            for r in result[0]:
                ocr_text.append(r[1][0])
        else:
            ocr_text = "No text detected."

        if debug:
            self.show_img_with_ocr()

        return ocr_text
    
    def show_img_with_ocr(self):
        img = cv2.imread(self.img_path)
        roi_img = img.copy()

        for text_result in self.ocr_result:
            text = text_result[1][0]
            tlX = int(text_result[0][0][0])
            tlY = int(text_result[0][0][1])
            trX = int(text_result[0][1][0])
            trY = int(text_result[0][1][1])
            brX = int(text_result[0][2][0])
            brY = int(text_result[0][2][1])
            blX = int(text_result[0][3][0])
            blY = int(text_result[0][3][1])

            pts = ((tlX, tlY), (trX, trY), (brX, brY), (blX, blY))

            topLeft = pts[0]
            topRight = pts[1]
            bottomRight = pts[2]
            bottomLeft = pts[3]

            cv2.line(roi_img, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(roi_img, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(roi_img, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(roi_img, bottomLeft, topLeft, (0, 255, 0), 2)
            roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 20, font_size=15)
            # print(text)
        # plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))
        return roi_img
        
ocr = MyPaddleOCR()

# Function to ocr an image
def run_ocr(input_image,lang):#input_image, margin_ratio):
    try:
        ocr.change_model(lang)
        return ocr.run_ocr(input_image), ocr.show_img_with_ocr()
    except Exception as e:
        return f"An error occurred: {str(e)}",None

with gr.Blocks() as iface:
    with gr.Row():
        gr.Markdown("# paddleOCR")
    
    with gr.Column():
        input_image = gr.Image(type="filepath", label="Image")
        lang=gr.Dropdown(ocr.get_available_langs(),label="Language", info="Choose Language")
        button=gr.Button("OCR", variant="primary")

    button.click(fn=run_ocr,
                 inputs=[input_image,lang],
                 outputs=[gr.Text(label="Result"),gr.Image(label="Result")])

# Launch the Gradio web service
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",server_port=8080)
