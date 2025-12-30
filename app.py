import streamlit as st
from PIL import Image

import os
import io
import json
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

st.set_page_config(page_title = "Image to Recipe", layout='centered')

st.title("🧊 Image to Recipe")
st.write("Upload a photo of food or fridge contents.")

upload_image = st.file_uploader("Upload an image: ", type=['jpg', 'jpeg', 'png'])

def image_to_base64(image_bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

if upload_image:
    image_bytes = upload_image.getvalue()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption= 'Uploaded image', use_container_width=True)

    image_bytes = upload_image.read()
    image_base64 = image_to_base64(image_bytes)
    mime_type = upload_image.type

    with st.spinner("Analysing Image..."):
        response = client.responses.create(
            model = "gpt-4.1-mini",
            input = [
                {
                    'role': 'user',
                    'content': [
                        {
                        'type': 'input_text',
                        'text': 'Identify all visible food ingredients in this image'
                        'Return only in valid JSON format:' '{"ingredients": ["item1", "item2"]}'
                        },
                        {
                            'type': 'input_image',
                            "image_url": f"data:{mime_type};base64,{image_base64}"
                        }
                    ]
                }
            ]
        )

        raw_output = response.output_text

    try:
        ingredients_data = json.loads(raw_output)
        ingredients = ingredients_data.get('ingredients', [])
    except json.JSONDecodeError:
        st.error('Failed to parse ingredients')
        st.stop()

    st.subheader('Ingredients Detected')
    st.write(ingredients)