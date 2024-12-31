from app import app
import requests

@app.get("/GET_API_STATUS")
def get_ApiEstatus():
    return {"status": "API is running"}