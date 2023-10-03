import os
import gradio as gr
import torch
from transformers import pipeline,AutoTokenizer, AutoModelForSeq2SeqLM

# required to install the following libraries
# pip install sacremoses sentencepiece

langs = ["en", "zh", "ko","jp","fr","ru"]
cur_src = langs[2]
cur_tat = langs[0]

pipe = None

def change_pipe(source,target):
    model_id = "Helsinki-NLP/opus-mt-{0}-{1}".format(source,target)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

    global pipe
    pipe = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
    )

change_pipe(cur_src,cur_tat)

def translate(src,target,text):
    try:
        global cur_src, cur_tat, pipe
        # change model
        if src and target and \
           (src != cur_src or target != cur_tat):
            change_pipe(src,target)
            cur_src=src
            cur_tat=target
        return pipe(text)[0]["translation_text"]
    except Exception as e:
        return str(e)

demo = gr.Interface(
    translate,
    inputs=[gr.Dropdown(langs,label="Source", info="Choose Language"),gr.Dropdown(langs,label="Target", info="Choose Language"),"text"],
    outputs="text",
    description="Multi-Lingual Translator"
    )

demo.launch(debug=True, server_name="0.0.0.0", server_port=8080)