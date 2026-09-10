from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'model'))
from captcha_model import predict

app=FastAPI(title='CAPTCHA Recognition API', version='1.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

@app.get('/health')
def health(): return {'status':'ok'}

@app.post('/predict')
async def predict_captcha(file: UploadFile = File(...)):
    if not (file.content_type or '').startswith('image/'):
        raise HTTPException(400,'Please upload an image file.')
    data=await file.read()
    try: img=Image.open(BytesIO(data))
    except Exception: raise HTTPException(400,'Invalid image.')
    return predict(img)
