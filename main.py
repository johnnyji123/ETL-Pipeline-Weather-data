import requests
import mysql.connector
import pandas as pd
import polars as pl
import json


db = mysql.connector.connect(
    
        host = "localhost",
        user = "root",
        password = "projects123123",
        database = "weather_pipeline"
    )

cursor = db.cursor()

# table weather_pipeline

api_key = "f5dd56508e67c163c95b7ed93bbc5dcb"


url = f"https://api.openweathermap.org/data/2.5/weather?q=london&appid={api_key}&units=metric"

response = requests.get(url)    
data = json.loads(response.text)
df = pd.DataFrame(data['main'], index = [0])



current_weather = data['main']
current_weather

keys = []
values = []

def extract_key_values(weather_dict):
    for key, value in weather_dict.items():
        keys.append(key)
        values.append(value)
        
extract_key_values(current_weather)

