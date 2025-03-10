# filepath: ProVisionAI/frontend/app.py
import streamlit as st
import requests
from PIL import Image
import io

st.title("ProVisionAI")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    
    response = requests.post('http://localhost:5000/annotate', json={
        'image': img_byte_arr.decode('latin1')
    })

    try:
        json_response = response.json()
        if response.status_code == 200:
            st.write(json_response)
        else:
            st.write("Error:", json_response)
    except requests.exceptions.JSONDecodeError:
        st.write("Error: API returned an empty or invalid response")
        json_response = None
    
    
    
