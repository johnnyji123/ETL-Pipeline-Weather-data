### Data Pipeline for Weather Data
### Overview: This project demonstrates the creation of a data pipeline for retrieving weather data from the OpenWeatherMap API, processing it, and storing it in a MySQL database. The pipeline is automated using the APScheduler library, ensuring regular updates of weather information.

### Process
* A call is made to OpenWeatherMap API to fetch weather data in London
* This data is processed and stored in a MySQL database
* SQL query is written to update the database with the current weather data
* This project demonstrates the use of cron, a time-based job scheduler, to automate and schedule recurring tasks, such as running scripts, fetching data, and executing commands at specified intervals
* APScheduler library is used to automate this process - The database will update with the current weather data every day at 6:30PM

### ETL error handling (Extract, Transform, Load)
* The core function responsible for fetching weather data from the OpenWeatherMap API, get_weather_data(url), is wrapped in a try-except block.
* If an exception occurs during the API call, a detailed error message is printed to the console, aiding in troubleshooting and debugging.
* In addition to console logging, an email notification is sent to a specified email address using the smtplib library. The notification includes information about the error, allowing for immediate attention and resolution.

### Benefits
* Email notifications enable swift awareness of any ETL errors, facilitating prompt investigation and resolution.
* By handling errors gracefully, the data pipeline maintains a high level of reliability, ensuring uninterrupted data processing.
