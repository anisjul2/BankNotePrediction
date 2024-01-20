# importing libraries1
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd 

#create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return{'message': 'Hello, stranger'}


@app.get('/{name}')
def get_name(name:str):
    return{'message': f'Hello,{name}'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    #print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction= classifier.predict([[variance,skewness,curtosis,entropy]])
    if (prediction[0]>0.5):
        prediction='fake note'
    else:
        prediction='its a bank note'
    return{
        'prediction': prediction

    }

if __name__ =='main':
    uvicorn.run(app.host-'127.0.0.1',port-8000)
