from flask import Flask, request, jsonify
from PIL import Image
from start import *
import tempfile
from received import *
import os


app = Flask(__name__)

def is_valid_move(move):
    # Add your custom logic to validate a chess move
    # For simplicity, checking if the move is two characters
    return len(move) == 2

def extract_moves(data):
    moves = [data[i:i+2] for i in range(0, len(data), 2)]
    return moves if all(is_valid_move(move) for move in moves) else None

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
@app.route('/chessmove', methods=['POST'])
def chess_move():
    if request.method == 'POST':
        data = request.form.get('move')

        if data is None or data.strip() == '':
            return "Chess move data is empty"

        extracted_moves = extract_moves(data)

        if extracted_moves is None or len(extracted_moves) != 2:
            return "Invalid chess move data. Please provide exactly two valid moves."

        move1, move2 = extracted_moves
        received(move1+move2)
        
        return f"Received chess moves: {move1}, {move2}"
    else:
        return "Invalid request method"

if __name__ == '__main__':
    initial_array_path = 'initial_array.pkl'
    if os.path.exists(initial_array_path):
        os.remove(initial_array_path)
    app.run( host='0.0.0.0', port=9081)
