from fastapi import FastAPI
from routes import router

app = FastAPI(title="Smart Attendance API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Attendance System Running"}
