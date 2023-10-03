import gradio as gr

from pdf2docx import Converter

def run(pdf):
    try:
        docx_file="/tmp/pdf2doc.output.docx"

        cv = Converter(pdf)
        
        # # convert from the second page to the end (by default)
        # cv.convert(docx_file, start=1)

        # # convert from the first page (by default) to the third (end=3, excluded)
        # cv.convert(docx_file, end=3)

        # # convert from the second page and the third
        # cv.convert(docx_file, start=1, end=3)

        # # convert the first, third and 5th pages
        # cv.convert(docx_file, pages=[0,2,4])
        
        # cv = Converter(pdf_file, password)

        cv.convert(docx_file)
        return docx_file
    except Exception as e:
        return None

demo = gr.Interface(
    run,
    inputs=gr.File(type="file",label="PDF file",format="pdf"),
    outputs=gr.File(type="file",label="Docx file",format="docx"))

# Launch the Gradio web service
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",server_port=8080)