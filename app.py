import flask
from flask import Flask,render_template,request
import numpy as np
import pickle

with open('MP_MODEL.pkl','rb') as f:
    model=pickle.load(f)

m_values=np.array(model["m_values"])
C=model["intercept"]

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features=[float(i) for i in request.form.values()]
    features=np.array(features)

    prediction=C+np.dot(features,m_values)

    return render_template('index.html',prediction_text=round(prediction,2))

if __name__=='__main__':
    app.run(debug=True)
