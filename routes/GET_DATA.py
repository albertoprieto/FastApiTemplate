from app import app
import requests

@app.get("/GET_DATA")
def get_ApiEstatus():
    return {"data": "data"}