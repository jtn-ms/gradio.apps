#-*- coding:utf-8 -*-
import os
import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob

from flask import Flask, request, render_template, jsonify
from PIL import Image
import base64

from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.abspath('uploads')
app.config['WEBFILE_FOLDER'] = os.path.abspath('webfiles')
app.config["CACHE_TYPE"] = "null"
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024    # 1 Mb limit

app.filename = ""

app.results = []
app.image_fn = os.path.join(app.config['UPLOAD_FOLDER'], "image.jpg")
app.result_fn = os.path.join(app.config['UPLOAD_FOLDER'], "result.txt")
app.result_dir = './test_result'

# Define a route for uploading an image
@app.route('/', methods=['POST'])
def upload_image():
    try:
        # Get the uploaded file
        uploaded_file = request.files['file']

        # Check if the file is empty
        if uploaded_file.filename == '':
            return jsonify({'error': 'No file selected'})

        # check if file is valid
        if not uploaded_file: return

        # save uploaded to local file system
        filename = secure_filename(uploaded_file.filename)
        app.filename = filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], app.filename)
        uploaded_file.save(file_path)

        # Read the image using PIL (Pillow)
        image = np.array(Image.open(file_path).convert('RGB'))
        t = time.time()
        result, image_framed = ocr.model(image)
        #output_file = os.path.join(app.result_dir, uploaded_file.split('/')[-1])
        #Image.fromarray(image_framed).save(output_file)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")
        for key in result:
            print(result[key][1])

        app.results += [result[key][1] for key in result]

        # Convert the image to base64 for display
        img_data = base64.b64encode(uploaded_file.read()).decode()

        return render_template('result.html', results="".join(app.results))
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Serve an HTML page for file upload
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# from flask import send_from_directory

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):

#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

# from werkzeug import SharedDataMiddleware
# app.add_url_rule('/uploads/<filename>', 'uploaded_file',
#                  build_only=True)
# app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
#     '/uploads':  app.config['UPLOAD_FOLDER']
# })

if __name__ == '__main__':
    if os.path.exists(app.result_dir):
        shutil.rmtree(app.result_dir)
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])
    os.mkdir(app.result_dir)
    os.mkdir(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=8080, debug=True)
