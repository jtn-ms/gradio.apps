from flask import Flask, request, jsonify
from PIL import Image
from deepface import DeepFace
import numpy as np

import json

class CustomJSONizer(json.JSONEncoder):
    def default(self, obj):
        return super().encode(bool(obj)) \
            if isinstance(obj, np.bool_) \
            else super().default(obj)
    
app = Flask(__name__)

backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
]

@app.route('/sort', methods=['POST'])
def sort():
    try:
        for file_key in request.files:
            uploaded_file = request.files[file_key]

            if uploaded_file.filename == '':
                continue

            img = Image.open(uploaded_file.stream)

        return jsonify({'results': "This api is not ready for use"})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/verify', methods=['POST'])
def verify():
    try:
        uploaded_file1 = request.files['file1']
        uploaded_file2 = request.files['file2']

        if uploaded_file1.filename == '' or uploaded_file1.filename == '':
            return jsonify({'error': 'No file selected'})
        # Ensure that the uploaded file is an image (e.g., JPEG, PNG)
        if any([not f.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) for f in [uploaded_file1,uploaded_file2]]):
            return jsonify({'error': 'Unsupported file format'})
        
        resp_obj = DeepFace.verify(img1_path=np.array(Image.open(uploaded_file1.stream)), img2_path=np.array(Image.open(uploaded_file2.stream)))
        return jsonify({'results': json.dumps(resp_obj, cls=CustomJSONizer)})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/embedding', methods=['POST'])
def embedding():
    try:
        # Get the uploaded file
        uploaded_file = request.files['file']

        # Check if the file is empty
        if uploaded_file.filename == '':
            return jsonify({'error': 'No file selected'})

        # Ensure that the uploaded file is an image (e.g., JPEG, PNG)
        if not uploaded_file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return jsonify({'error': 'Unsupported file format'})
        
        embedding_objs = DeepFace.represent(img_path=np.array(Image.open(uploaded_file.stream)))

        return jsonify({'result': embedding_objs[0]["embedding"]})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get the uploaded file
        uploaded_file = request.files['file']

        # Check if the file is empty
        if uploaded_file.filename == '':
            return jsonify({'error': 'No file selected'})

        # Ensure that the uploaded file is an image (e.g., JPEG, PNG)
        if not uploaded_file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return jsonify({'error': 'Unsupported file format'})
        
        demographies = DeepFace.analyze(img_path=np.array(Image.open(uploaded_file.stream)),detector_backend = backends[3])

        return jsonify({'result': json.dumps(demographies, cls=CustomJSONizer)})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)