import fastapi
import uvicorn
import photo_data


app = fastapi.FastAPI()

@app.get('/')
def index():
    return{
        "message":"hello world"   
    }

@app.post('/image/')
def image_search(file: str = fastapi.Form(...)):
    return photo_data.get_image(file)

@app.get('/image/{file}')
def image_search(file: str):
    return photo_data.get_image(file)

@app.get('/image/duplicates/')
def image_search():
    return photo_data.get_duplicates_all()

@app.get('/metrics')
def get_metrics():
    return photo_data.get_metrics()


if __name__ == '__main__':
    print('Setting the API to the Background:')
    uvicorn.run(app)
    
    
