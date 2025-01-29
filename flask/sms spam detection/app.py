import os
from pyexpat import model
from numpy import vectorize 
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
import pickle as pkl
cv = pkl.load(open('C:\Users\Kethavath Sunitha\Desktop\sms spam detection\spam-sms-mnb-model.pkl','rb'))
classifier = pkl.load(open('C:\Users\Kethavath Sunitha\Desktop\sms spam detection\spam-sms-mnb-model.pkl','rb'))
app = Flask(__SMS SPAM DETECTION__) # type: ignore
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/spamdetection1')
def spamdetection1():
    return render_template('spamdetection1.html')
# @app.route('/spam',methods=['POST','GET'])
# def prediction():
#    return render_template('spam.html')
@app.route('/predict1')
def predict1():
    return render_template('predict1.html')
@app.route('/predict2')
def predict2():
    return render_template('predict2.html')
@app.route('/predict',methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]    
        vect = cv.transform(data).toarray()  
        my_prediction = classifier.predict(vect)  
        return render_template('result.html', prediction=my_prediction)
if __name__=="__main__":
    app.run(debug=True)