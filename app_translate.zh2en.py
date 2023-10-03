import os
import gradio as gr
import torch
from transformers import pipeline,AutoTokenizer, AutoModelForSeq2SeqLM

# required to install the following libraries
# pip install sacremoses sentencepiece
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

translator = pipeline(
    "translation",
    model=model,
    tokenizer=tokenizer,
)

def translate(text):
    try:
        return translator(text)[0]["translation_text"]
    except Exception as e:
        return str(e)

demo = gr.Interface(
    translate,
    inputs="text",
    outputs="text",
    description="Chinese To English"
    )

demo.launch(debug=True, server_name="0.0.0.0", server_port=8080)