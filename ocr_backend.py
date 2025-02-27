import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract
import tempfile
import os

# Set up Tesseract OCR path (Update this path if needed)
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = TESSERACT_PATH


def capture_image():
    """Capture an image using webcam and save it."""
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise Exception("Could not access the webcam. Make sure it's connected and not used by another app.")

    while True:
        ret, frame = camera.read()
        if not ret:
            raise Exception("Failed to capture image from webcam.")
        
        cv2.imshow("Press 'D' to Capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('d'):
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            break
    
    camera.release()
    cv2.destroyAllWindows()
    
    return image_path


def extract_text(image_path):
    """Extract text from an image using Tesseract OCR."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' not found.")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error loading image. The file may be corrupted or not a valid image format.")
    
    text = pytesseract.image_to_string(image)
    return text
