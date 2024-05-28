from pydantic import BaseModel

class InputData(BaseModel):
    WhiteElo: int
    WhiteRatingDiff: int
    White_playTime_total: int
    White_count_all: int
    BlackElo: int
    BlackRatingDiff: int
    Black_playTime_total: int
    Black_count_all: int
    TotalMoves: int
    TimeControl: int


class PredictionResponse(BaseModel):
    result: float
