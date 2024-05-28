from fastapi import FastAPI
from app.model import predict_result
from app.schema import InputData, PredictionResponse

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
async def predict(data: InputData):
    prediction = predict_result(data)
    return PredictionResponse(result=prediction)
