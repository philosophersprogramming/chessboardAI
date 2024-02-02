from flask import Flask, request, jsonify
from PIL import Image
from start import *
from received import *
import tempfile
import os

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_image():
    try:
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
    except Exception as e:
        print(f"Error in /upload: {e}")
        return jsonify({'error': 'Internal server error'})

@app.route('/chessmove', methods=['POST'])
def chess_move():
    try:
        if request.method == 'POST':
            data = request.form.get('move')

            received(data)
            
            return f"Received chess moves: {data}"
        else:
            return "Invalid request method"
    except Exception as e:
        print(f"Error in /chessmove: {e}")
        return jsonify({'error': 'Internal server error'})

@app.route('/gamestat', methods=['POST'])
def gamestat():
    # Get the form data from the request

    # gameid = request.form.get('gameid', '')
    # Access specific form fields
    gamestats = request.form.get('reset', '')
    
    if gamestats.upper() == 'TRUE': 
        print("RESETTING")
        if os.path.exists(initial_array_path):
            os.remove(initial_array_path)
    
    # Do something with the form data (e.g., print it)
    print("Received form data - Text field:")
    
    # Return a response
    return "Form data received successfully"

if __name__ == '__main__':
    initial_array_path = 'initial_array.pkl'
    if os.path.exists(initial_array_path):
        os.remove(initial_array_path)
    app.run(host='0.0.0.0', port=9081)
