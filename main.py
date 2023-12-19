import requests
import mysql.connector
import pandas as pd
import polars as pl
import json
from apscheduler.schedulers.background import BlockingScheduler
import smtplib

# Connecting to database
db = mysql.connector.connect(
    
        host = "localhost",
        user = "root",
        password = "password",
        database = "weather_pipeline"
    )


# Creating a cursor object
cursor = db.cursor()

# Open weather API key
api_key = "api_key"

# Fetching data from API - handling ETL failure     
def get_weather_data(url):
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        weather_data = data['main']
        return weather_data
    
    except Exception as e:
        from_email = "example@gmail.com"
        to_email = "example@hotmail.com"
        message = "Could not retrieve data from API",e

        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(from_email, "password")
        smtp_server.sendmail(from_email, to_email, message)

        
# Calling weather data
weather_data = get_weather_data(f"https://api.openweathermap.org/data/2.5/weather?q=london&appid={api_key}&units=metric")


        
keys = []
values = [] 

# Storing the values in weather_data dictionary in a list        
def extract_key_values(weather_data):
    for key, value in weather_data.items():
        keys.append(key)
        values.append(value)
        
extract_key_values(weather_data)


# Update database with the current weather data
def update_weather_data():
    update = "UPDATE weather_pipeline SET temp = %s, feels_like = %s, temp_min = %s, temp_max = %s, pressure = %s, humidity = %s WHERE id = 001"  
    cursor.execute(update, values)
    db.commit()
    


# Automating the process - database automatically updated
scheduler = BlockingScheduler()
scheduler.add_job(update_weather_data, 'cron', hour = 18, minute = 30)
scheduler.start()


