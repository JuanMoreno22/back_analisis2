import joblib
import pandas as pd
import os
from app.schema import InputData

# Obtener la ruta absoluta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'modelo.pkl')

# Cargar el modelo desde el archivo
model = joblib.load(model_path)

def create_input_dataframe(data: InputData):
    input_dict = {
        'WhiteElo': data.WhiteElo,
        'WhiteRatingDiff': data.WhiteRatingDiff,
        'White_playTime_total': data.White_playTime_total,
        'White_count_all': data.White_count_all,
        'BlackElo': data.BlackElo,
        'BlackRatingDiff': data.BlackRatingDiff,
        'Black_playTime_total': data.Black_playTime_total,
        'Black_count_all': data.Black_count_all,
        'TotalMoves': data.TotalMoves,
        'TimeControl': data.TimeControl,

    }
    df_entrada = pd.DataFrame([input_dict])
    return df_entrada

def predict_result(data: InputData) -> float:
    df_entrada = create_input_dataframe(data)
    prediction = model.predict(df_entrada)
    return prediction[0]
