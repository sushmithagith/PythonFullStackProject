# API/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import sys, os
from datetime import datetime
from typing import List


# Import Monitor from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import Monitor

# ---------------- App Setup ----------------
app = FastAPI(title="Silent Classroom Monitor", version="1.0")

# Allow Frontend (Streamlit/React) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- Monitor Instance --------------
monitor = Monitor()  # create an instance

# ----------- Data Models -------------------
class CreateNoise(BaseModel):
    Classroom: str
    Teacher: str
    noise_level: float = 0
    low_threshold: float = 50
    high_threshold: float = 75
    timeStamp: datetime = None


class NoiseUpdate(BaseModel):
    completed: bool


class CreateReport(BaseModel):
    report_date: datetime
    Classroom: str
    Teacher: str
    noise_readings: List[float] = []
    high_threshold: float = 75


class UpdateReport(BaseModel):
    avg_noise: float = None
    max_noise: float = None
    violations: int = None

# --------------- Endpoints ----------------
@app.get("/")
def home():
    """Check if the API is running"""
    return {"message": "Silent Classroom Monitor is running!"}

# -------- NoiseLogs Endpoints -------------
@app.get("/NoiseLogs")
def get_noise():
    return monitor.get_noise()

@app.post("/NoiseLogs")
def create_noise(cn: CreateNoise):
    result = monitor.add_noise(
        cn.Classroom,
        cn.Teacher,
        cn.noise_level,
        cn.low_threshold,
        cn.high_threshold,
        cn.timeStamp
    )
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/NoiseLogs/{Id}")
def update_noise(Id: int, cn: NoiseUpdate):
    result = monitor.noise_update(Id) if cn.completed else monitor.mark_pending(Id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/NoiseLogs/{Id}")
def delete_noise(Id: int):
    result = monitor.delete_noise(Id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

# -------- Reports Endpoints -------------
@app.get("/Reports")
def get_reports():
    return monitor.get_reports()

@app.post("/Reports")
def create_report(rp: CreateReport):
    result = monitor.add_report(
        rp.report_date,
        rp.Classroom,
        rp.Teacher,
        rp.noise_readings,
        rp.high_threshold
    )
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/Reports/{report_id}")
def update_report(report_id: int, data: UpdateReport):
    # Only include fields that are not None
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    result = monitor.update_report(report_id, update_data)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/Reports/{report_id}")
def delete_report(report_id: int):
    result = monitor.delete_report(report_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result
