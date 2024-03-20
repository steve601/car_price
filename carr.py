from flask import Flask,request,render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('car.pkl','rb'))

@app.route('/')
def home():
    return render_template('car.html')

@app.route('/predict', methods = ['POST'])
def predict():
    a = request.form['Year']
    b = float(request.form['Present_Price'])
    c = float(request.form['Kms_Driven'])
    d = request.form['Fuel_Type']
    e = request.form['Seller_Type']
    f = request.form['Transmission']
    
    if d == 'Petrol':
        d=2
    if d == 'Diesel':
        d=1
    if d == 'CNG':
        d=0
        
    if e == 'Dealer':
        e=1
    if e == 'Individual':
        e=0
        
    if f == 'Manual':
        f=1
    if f == 'Automatic':
        f=0
        
    arr = np.array([[a,b,c,d,e,f]])
    prediction = model.predict(arr)
    prediction = np.round(prediction,2)
    
    text = f'You can sell your car for ${prediction}'
    
    return render_template('car.html',pred = text)

if __name__ == '__main__':
    app.run(debug=True)
    
    