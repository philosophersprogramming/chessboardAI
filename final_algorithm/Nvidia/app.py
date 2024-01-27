from flask import Flask, request, jsonify
from PIL import Image
from start import *
import tempfile
import os


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    print("Request data:", request.data)
    print("Request form:", request.form)
    print("Request files:", request.files)

    # Check if the post request has the file part
    if 'file' not in request.files:
        print("No file part")
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        print("No selected file")
        return jsonify({'error': 'No selected file'})

    temp_filename = os.path.join(tempfile.gettempdir(), file.filename)
    file.save(temp_filename)
    # Process the image (you may want to do more meaningful processing here)
    # img = Image.open(file)
    # img.show()

    output = start(temp_filename)
    return jsonify(output)

if __name__ == '__main__':
    initial_array_path = 'initial_array.pkl'
    if os.path.exists(initial_array_path):
        os.remove(initial_array_path)
    app.run( host='0.0.0.0', port=9081)
