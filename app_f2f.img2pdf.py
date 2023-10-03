import gradio as gr

from pathlib import Path
import img2pdf

def run(files):
    try:
        pdf_file="/tmp/img2pdf.output.pdf"

        with open(pdf_file,"wb") as f:
            f.write(img2pdf.convert(files))#[str(path) for path in Path('./Final').glob('*.png')]))

        return pdf_file
    except Exception as e:
        return None

demo = gr.Interface(
    run,
    inputs=gr.File(file_count="multiple",label="Image file",file_types=[".jpeg", ".png", ".jpg"]),
    outputs=gr.File(type="file",label="PDF file",format="pdf"))

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)