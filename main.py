import requests
import mysql.connector
import pandas as pd
import polars as pl
import json



api_key = "f5dd56508e67c163c95b7ed93bbc5dcb"


url = f"https://api.openweathermap.org/data/2.5/weather?q=london&appid={api_key}"

response = requests.get(url)    
data = json.loads(response.text)
df = pd.DataFrame(data['main'], index = [0])
df