from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class DataRequest(BaseModel):
    data: List[str]

@app.post("/bfhl")
def process_data(request: DataRequest):
    user_id = "22BDA70168"
    email = "shubhamsourav475@gmail.com"
    roll_number = "70168"
    
    numbers = [item for item in request.data if item.isdigit()]
    alphabets = [item for item in request.data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []
    
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    return response

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
