
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
classifier_DT = pickle.load(open('P7decision_model.pkl','rb')) 
classifier_SVM =pickle.load(open('P7SVM_model.pkl','rb')) 
classifier_DT = pickle.load(open('P7decision_model.pkl','rb')) 
classifier_KNN = pickle.load(open('P7KNN_model.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict1',methods=['GET'])
def predict1():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = int(request.args.get('exp1'))
    exp2 = int(request.args.get('exp2'))
    exp3 = int(request.args.get('exp3'))
    exp4 = int(request.args.get('exp4'))
    exp5 = int(request.args.get('exp5'))
    exp6 = int(request.args.get('exp6'))
    exp7 = int(request.args.get('exp7'))
    exp8 = int(request.args.get('exp8'))
    exp9 = int(request.args.get('exp9'))
    exp10 = int(request.args.get('exp10'))

    prediction1 = classifier_DT.predict([[exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10]])
    if prediction1==[0]:
      prediction1='Customer will  close acconut'
    else:
      prediction1='Customer will not  close acconut'

        
    return render_template('index.html', prediction_text=' Model  has predicted that : {}'.format(prediction1))


@app.route('/predict2',methods=['GET'])
def predict2():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = int(request.args.get('exp1'))
    exp2 = int(request.args.get('exp2'))
    exp3 = int(request.args.get('exp3'))
    exp4 = int(request.args.get('exp4'))
    exp5 = int(request.args.get('exp5'))
    exp6 = int(request.args.get('exp6'))
    exp7 = int(request.args.get('exp7'))
    exp8 = int(request.args.get('exp8'))
    exp9 = int(request.args.get('exp9'))
    exp10 = int(request.args.get('exp10'))

    prediction2 = classifier_SVM.predict([[exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10]])
    if prediction2==[0]:
      prediction2='Customer will  close acconut'
    else:
      prediction2='Customer will not close acconut'
        
    return render_template('index.html', prediction_text=' Model  has predicted that : {}'.format(prediction2))



@app.route('/predict3',methods=['GET'])
def predict3():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = int(request.args.get('exp1'))
    exp2 = int(request.args.get('exp2'))
    exp3 = int(request.args.get('exp3'))
    exp4 = int(request.args.get('exp4'))
    exp5 = int(request.args.get('exp5'))
    exp6 = int(request.args.get('exp6'))
    exp7 = int(request.args.get('exp7'))
    exp8 = int(request.args.get('exp8'))
    exp9 = int(request.args.get('exp9'))
    exp10 = int(request.args.get('exp10'))

    prediction3 = classifier_Random.predict([[exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10]])
    
    if prediction3==[0]:
      prediction3='Customer will  close acconut'
    else:
      prediction3='Customer will not close acconut'
        
    return render_template('index.html', prediction_text=' Model  has predicted that : {}'.format(prediction3))




@app.route('/predict4',methods=['GET'])
def predict4():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = int(request.args.get('exp1'))
    exp2 = int(request.args.get('exp2'))
    exp3 = int(request.args.get('exp3'))
    exp4 = int(request.args.get('exp4'))
    exp5 = int(request.args.get('exp5'))
    exp6 = int(request.args.get('exp6'))
    exp7 = int(request.args.get('exp7'))
    exp8 = int(request.args.get('exp8'))
    exp9 = int(request.args.get('exp9'))
    exp10 = int(request.args.get('exp10'))

    prediction4 = classifier_KNN.predict([[exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10]])
    if prediction4==[0]:
      prediction4='Customer will  close acconut'
    else:
      prediction4='Customer will not close acconut'

        
    return render_template('index.html', prediction_text=' Model  has predicted that : {}'.format(prediction4))


if __name__ == "__main__":
    app.run(debug=True)