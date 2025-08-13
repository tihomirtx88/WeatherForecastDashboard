from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_data(place, forecast_days=None, kind=None):
    api_key = os.getenv("API_KEY");
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url);
    data = response.json();
    return data

if __name__ == "__main__":
    print(get_data(place="Sofia"));