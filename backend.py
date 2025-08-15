from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_data(place, forecast_days=None):
    api_key = os.getenv("API_KEY");
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url);
    data = response.json();
    filtered_data = data["list"];
    # filterenig days
    nr_values = 8 * forecast_days;
    filtered_data = filtered_data[:nr_values];
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Sofia", forecast_days=3));