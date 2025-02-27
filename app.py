import streamlit as st
import numpy as np
import cv2
from PIL import Image
from ocr_backend import extract_text  # Importing OCR function from backend

st.title("📷 Live Text Detection using OCR")
st.write("Capture an image using your webcam or upload an image.")

# Camera Input for live capture
captured_image = st.camera_input("Take a picture")

# File Uploader for manual image upload
uploaded_file = st.file_uploader("Or Upload an Image", type=["jpg", "png", "jpeg"])

# Process Image (either from camera or uploaded file)
if captured_image or uploaded_file:
    # Load the image
    if captured_image:
        image = Image.open(captured_image)
    else:
        image = Image.open(uploaded_file)

    st.image(image, caption="Captured Image", use_container_width=True)

    # Save image temporarily for OCR processing
    image_np = np.array(image)
    image_path = "temp_image.jpg"
    cv2.imwrite(image_path, cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))

    # Extract text using OCR
    extracted_text = extract_text(image_path)
    
    st.subheader("📝 Extracted Text:")
    st.write(extracted_text)
