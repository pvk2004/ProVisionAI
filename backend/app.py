# import os
# import base64
# import requests
# from PIL import Image
# import io
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from dotenv import load_dotenv

# load_dotenv()  # Load API key from .env file

# app = Flask(__name__)
# CORS(app)

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# API_URL = os.getenv("API_URL")

# @app.route('/annotate', methods=['POST'])
# def annotate():
#     image_data = request.json.get('image')
#     # image_data = Image.open(io.BytesIO(base64.b64decode(request.json.get('C:/Users/vamsh/OneDrive/Pictures/download.jpg'))))
#     if not image_data:
#         return jsonify({'error': 'No image data provided'}), 400

#     try:
#         annotation = annotate_image(image_data)
#         return jsonify(annotation)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# def annotate_image(image_data):
#     response = requests.post(
#         API_URL,
#         headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
#         json={
#             "contents": [
#                 {
#                     "parts": [
#                         {
#                             "mimeType": "image/png",
#                             "data": base64.b64encode(image_data).decode("utf-8")  
#                         }
#                     ]
#                 }
#             ]
#         },
#         # json={"inputs": image_data},
#         params={"key": GEMINI_API_KEY} 
#     )
#     response.raise_for_status()
#     # print("Raw Response:", response.text)

#     return response.json()

# # def annotate_image(image_data):
# #     response = requests.post('https://gemini-vision-pro-api-url', json={
# #         'apiKey': os.getenv('GEMINI_VISION_API_KEY'),
# #         'image': image_data  # ✅ Send base64 string directly
# #     })
# #     response.raise_for_status()
# #     return response.json()


# if __name__ == '__main__':
#     app.run(debug=True)
import os
import base64
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = os.getenv("API_URL")

@app.route('/annotate', methods=['POST'])
def annotate():
    data = request.json.get('image')  
    if not data:
        return jsonify({'error': 'No image data provided'}), 400
    
    try:
        # Decode the base64 string from frontend
        image_bytes = base64.b64decode(data)
        
        # Re-encode it properly to base64 before sending to Gemini
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")

        annotation = annotate_image(encoded_image)
        return jsonify(annotation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def annotate_image(image_data):
    response = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
        json={
            "contents": [
                {
                    "parts": [
                        {
                            "mimeType": "image/png",
                            "data": image_data  # Send properly encoded base64
                        }
                    ]
                }
            ]
        }
    )
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
