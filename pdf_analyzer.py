from operator import imod
import numpy as np
import cv2
import requests
from pdf2image import convert_from_path
from random import randint

def pdf_to_image(filepath):
    page = convert_from_path(filepath, poppler_path=r'C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin')
    ran = randint(0,10000)
    page[0].save(f'usecases/use_case_{ran}.jpg', 'JPEG')
    return f'usecases/use_case_{ran}.jpg'


def analyze_usecase(image_url):
    headers = {
        'Prediction-Key': "78abf120e34b4fa0881c074ffa2b564b",
        'Content-Type': "application/json",
    }
    data = {"Url": image_url}

    url = "https://umlcount.cognitiveservices.azure.com/customvision/v3.0/Prediction/f5738398-f490-46f9-9a78-7fdddb364ce1/detect/iterations/Cost%20Estimation/url"

    r = requests.post(url=url,  headers=headers, json=data)
    return r.json()