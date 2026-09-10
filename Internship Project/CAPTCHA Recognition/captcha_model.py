"""CAPTCHA inference module.
Drop-in replacement for the missing best_model.hdf5 artifact from the legacy notebook.
Uses Tesseract OCR with CAPTCHA-specific preprocessing; no training step is required.
"""
import re, tempfile, os
from PIL import Image, ImageOps, ImageFilter
import pytesseract

ALLOWED = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def predict(image: Image.Image):
    image = image.convert("L").resize((320,120))
    image = ImageOps.autocontrast(image)
    image = image.filter(ImageFilter.MedianFilter(3))
    # threshold for CAPTCHA text
    image = image.point(lambda p: 0 if p < 180 else 255)
    text = pytesseract.image_to_string(
        image,
        config='--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )
    text = re.sub(r'[^0-9A-Za-z]', '', text)
    text = text[:6]
    return {"prediction": text, "confidence": None}
