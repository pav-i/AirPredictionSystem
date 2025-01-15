from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 'random_forest_regression_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        t = int(request.form['T'])
        tm = int(request.form['TM'])
        tmm = int(request.form['Tm'])
        slp = int(request.form['SLP'])
        h = int(request.form['H'])
        vv = float(request.form['VV'])
        v = float(request.form['V'])
        vm = int(request.form['VM'])
        
        data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
        my_prediction = classifier.predict(data)
        predicted_aqi = my_prediction[0] 

        if predicted_aqi <= 50:
            category = "Good"
        elif predicted_aqi <= 100:
            category = "Satisfactory"
        elif predicted_aqi <= 150:
            category = "Alert"
        
        else:
            category = "Hazardous"

        return render_template('result.html', prediction=[predicted_aqi], category=category)

if __name__ == '__main__':
    app.run(debug=True)
