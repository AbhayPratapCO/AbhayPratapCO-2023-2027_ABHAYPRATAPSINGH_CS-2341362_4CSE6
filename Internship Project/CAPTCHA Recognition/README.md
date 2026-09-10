# CAPTCHA Recognition Web App

A portfolio-ready web wrapper around a CAPTCHA recognition pipeline. The legacy notebook uses a MobileNet-based multi-character classifier, 60x160 grayscale inputs and 4–6 character outputs. The uploaded notebook does not contain the saved `best_model.hdf5` weights, so this deadline build uses a lightweight OCR inference adapter instead of claiming to reproduce unavailable weights.

## Run

1. Install Tesseract OCR and ensure `tesseract` is on PATH.
2. `pip install -r backend/requirements.txt`
3. `uvicorn backend.app:app --reload`
4. Open `frontend/index.html` in a browser.

API: `POST /predict` with form field `file`.
