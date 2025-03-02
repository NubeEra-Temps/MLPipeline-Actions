#!/usr/bin/env python
"""
A ML APPlication which predicts the profit of a StartUp based on certain features.

"""
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template


APP = Flask(__name__,template_folder='templates')
MODEL = ""
with open('model.pkl', 'rb') as file:
    MODEL = pickle.load(file)


@APP.route('/')
def home():
    '''
    Rendering Home Page
    '''
    return render_template('index.html')


@APP.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # features = [x for x in request.form.values()]
    features = list(request.form.values())
    final_features = [np.array(features)]
    column_names = ['R&D Spend', 'Administration', 'Marketing Spend', 'State']
    final_features = pd.DataFrame(final_features,columns=column_names)
    prediction = MODEL.predict(final_features)
    temp = 0.0
    for i in prediction:
        for j in i:
            temp = j
    # return render_template('index.html', prediction_text='${}'.format(temp))
    return render_template('index.html', prediction_text=f'${temp:.2f}')


if __name__ == '__main__':
    APP.run(host='0.0.0.0',port=8080)
