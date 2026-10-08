"""
Data-ontvanger (API).
Ontvangt sensordata die via een POST-request wordt gestuurd door het test-systeem.
"""
from fastapi import FastAPI

latest_data = None  # houdt de latest meting in het geheugen

app = FastAPI()

def parseData(data):
    if "battery_voltage" not in data:
        print("ontbrekend veld: battery_voltage")
        return

    global latest_data
    latest_data = data
    print("recentste meting bijgewerkt: ", latest_data)
    

@app.post("/data")
def ontvangData(data: dict):
    print(data)
    parseData(data)
    return {"status": "ok"}