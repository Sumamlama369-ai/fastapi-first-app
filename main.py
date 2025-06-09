from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message': "Welcome to Patient management System in FastAPI!"}

@app.get('/about')
def about():
    return {'message': "A fully functional API to manage your patient records"}

@app.get("/view")
def vide():
    data=load_data()
    return data