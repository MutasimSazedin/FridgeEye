# FridgeEye 🧊

FridgeEye is an AI-powered web app that turns photos of fridge contents into recipe suggestions.

The app uses computer vision to detect ingredients from real-world images and generates recipes while enforcing strict ingredient constraints.

## Features
- Upload photos of fridge contents or available ingredients
- Ingredient detection from images
- Recipe generation based on detected items
- Live deployment with Streamlit

## Tech Stack
- Python
- Streamlit
- OpenAI (multimodal models)

## Engineering Highlights
- Multimodal AI integration for image-based ingredient detection and recipe generation
- Strict JSON enforcement to prevent model output parsing errors
- Continuous Integration via GitHub Actions
- Containerized deployment support with Docker

## Running Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
## Live Demo
https://fridge-eye.streamlit.app
