# FridgeEye 🧊

FridgeEye is an AI-powered web app that turns photos of fridge contents into recipe suggestions.

The app uses computer vision to detect ingredients from real-world images and generates recipes while enforcing strict ingredient constraints.

## Features
- Upload fridge photos
- Ingredient detection from images
- Recipe generation based on detected items
- Live deployment with Streamlit

## Tech Stack
- Python
- Streamlit
- OpenAI (multimodal models)

## Running Locally
```bash
pip install -r requirements.txt
streamlit run app.py

## Live Demo
https://fridge-eye.streamlit.app
