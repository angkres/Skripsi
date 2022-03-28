from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, abort
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')
    


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        #f = load_img(file_path, target_size=(224, 224))
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        model = load_model('models/VGG16_Adam.h5')
 
        image = load_img(file_path, target_size=(224, 224))
        #image = load_img('drive/MyDrive/SkripsiData/trainKmeans/covid/segmentedKMeans_enhanced_1 (1500).jpg', target_size=(64, 64))

        img = np.array(image)
        img = img / 255.0
        img = img.reshape(1,224,224,3)
        label = model.predict(img)
        name1 = 'Normal\nAkurasi: '
        name2 = 'COVID-19\nAkurasi: '
        #labels=str(label[0][0])
        if label[0][0]> 0.5:
            hasil=str(label[0][0])
            labels=name1+hasil
        else:
            a=1-label[0][0]
            hasil=str(a)
            labels=name2+hasil
        return labels            
    return None
if __name__ == '__main__':
    app.run()
