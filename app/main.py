from typing import Optional

from fastapi import FastAPI, Form

app = FastAPI()

data = [{
 "id": "wBnmLMNkbsFErsjlDKWjA",
 "name": "oracle.jpeg",
 "image": 16384,
 "timestamp": "2021-06-08T13:52:28+00:00"
},
{
 "id": "fewfewfdsfsfsdfsdfsdfsd",
 "name": "monkey.jpeg",
 "image": 8064,
 "timestamp": "2021-07-08T13:52:28+00:00"
},{
 "id": "wBnmLMNkbsFErsjlDKWjA",
 "name": "oracle.jpeg",
 "image": 16384,
 "timestamp": "2021-06-08T13:52:28+00:00"
}
]

@app.get("/")
def read_root():
    return {"Nothing":"here!"}

@app.post('/image/')
def image_search(file: str = Form(...)):
    return get_image(file)

@app.get('/image/{file}')
def image_search(file: str):
    return get_image(file)

@app.get('/image/duplicates/')
def image_search():
    return get_duplicates_all()

@app.get('/metrics')
def get_metrics():
    return get_metrics()

def get_image(file : str):
    for x in data:
        if x['name'] == file:
            return x
    return 'Doesnt exist here!'

def get_duplicates_all():
    return ([objects for objects in data if data.count(objects) > 1])
