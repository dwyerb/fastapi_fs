from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    saxnet = "saxnet"
    marshall = "marshall"
    fender = "fender"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/models/{model_name}")
async def getModel(model_name:ModelName):
    if(model_name == ModelName.alexnet):
        return{"Model Name:":"Deep Learning"}
    if(model_name.value == 'saxnet'):
        return{"Model Name": model_name,"message":"LeCNN Something Something"}
    if (model_name == ModelName.marshall):
        return {"Model Name": model_name, "message": "We Are Marshall"}
    else:
        return {"Model Name": model_name, "message": "Sherd"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return{"Item ID:":item_id}