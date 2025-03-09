from flask import Flask, request, jsonify, render_template
import requests
import base64
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/annotate', methods=['POST'])
def annotate():
    image_data = request.json.get('image')
    if not image_data:
        return jsonify({'error': 'No image data provided'}), 400

    try:
        annotation = annotate_image(image_data)
        return jsonify(annotation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def annotate_image(image_data):
    # Decode the base64 image data
    image_data = base64.b64decode(image_data)
    response = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyC_McmuumJvA-3IBRFU3vB7d9NNwbRzb1w', json={
        'apiKey': os.getenv("AIzaSyC_McmuumJvA-3IBRFU3vB7d9NNwbRzb1w"),
        'image': image_data.decode('latin1')  # Ensure the image data is properly encoded
    })
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)