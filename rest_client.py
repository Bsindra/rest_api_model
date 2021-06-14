from flask_ngrok import run_with_ngrok
from flask import Flask , request
import numpy as np
import pickle
import os


path = os.path.dirname(os.path.abspath(__file__))

classifier_colab = pickle.load(open(path+'\classifier.pickle','rb'))
scaler_colab = pickle.load(open(path+'\sc.pickle','rb'))

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/predict',methods=['POST'])
def customer_behavior():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    print(age)
    print(salary)
    pred_proba = classifier_colab.predict_proba(scaler_colab.transform(np.array([[age,salary]])))[:,1]
    print(pred_proba)
    return "The prediction is {}".format(pred_proba)

app.run()
