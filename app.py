from itertools import count
import os
from xml.etree.ElementInclude import include
from flask import Flask, request
from pdf_analyzer import analyze_usecase, pdf_to_image
from firebase import upload_usecase
from handler import count_func, count_funct, find_complexity

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def process_pdf():
    usecase = request.files['usecase']
    filepath = 'usecases/'+usecase.filename
    usecase.save(filepath)
    jpg_loc = pdf_to_image(filepath)
    public_url = upload_usecase(filepath=jpg_loc)
    resp = analyze_usecase(image_url=public_url)
    
    usecases = count_func(resp['predictions'], 'usecase')
    actors = count_func(resp['predictions'], 'Actor')
    includes = count_funct(resp['predictions'], 'include')
    extends = count_funct(resp['predictions'], 'extent')

    usecase = {
        'usecases': usecases,
        'actors': actors,
        'includes': includes,
        'extends': extends 
    }

    complexity = find_complexity(usecases)

    if os.stat(filepath):
        os.remove(filepath)
    if os.stat(jpg_loc):
        os.remove(jpg_loc)
    
    return {
        'status': 'success',
        'status_code': 200,
        'usecase': usecase,
        'complexity': complexity
    }

app.run(host='localhost', port=8080)