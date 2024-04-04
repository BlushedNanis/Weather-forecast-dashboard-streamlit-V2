from os import getenv
from dotenv import load_dotenv
from requests import get


load_dotenv()


def get_forecast_data(place:str, days:int):
    """
    Sends a request to openweathermap.org to get the forecasted data for 
    the specified days and the specified kind. 

    Args:
        place (str): Name of the city to get weather data
        days (int): Numbers of day to forecast

    Returns:
        list: Forecasted data for the specified args.
    """
    #Make request and get content into a data variable in json format
    api_key = getenv("api_key")
    url = "https://api.openweathermap.org/data/2.5/forecast?q="\
    f"{place}&"\
    f"cnt={8 * days}&"\
    f"units=metric&"\
    f"appid={api_key}"
    response = get(url)
    data = response.json()
    
    weather_data = data["list"]
    city_data = data["city"]
    
    return data

def filter_data(data:dict):
    """Filters the given weather data to obtain temperatures, weather conditions,
    humidity and wind speed information.

    Args:
        data (dict): Weather data.

    Returns:
        dict: Filtered weather data.
        Keys: avg temperature, min temperature, max temperature, weather icons,
              weather description, humidity, wind speed, dates.
    """
    filtered_data = {}
    weather_data = data["list"]
    filtered_data["temperature"] = [dict["main"]["temp"]
                                        for dict in weather_data]
    filtered_data["feel temperature"] = [dict["main"]["feels_like"]
                                        for dict in weather_data]
    filtered_data["weather icons"] = [dict["weather"][0]["icon"]
                                      for dict in weather_data]
    filtered_data["weather description"] = [dict["weather"][0]["description"]
                                            for dict in weather_data]
    filtered_data["humidity"] = [dict["main"]["humidity"]
                                 for dict in weather_data]
    filtered_data["wind speed"] = [dict["wind"]["speed"]
                                   for dict in weather_data]
    filtered_data["dates"] = [dict["dt_txt"] for dict in weather_data]
    return filtered_data


if __name__ == "__main__":
    forecast = get_forecast_data("london", 2)
    print(forecast)
    print(filter_data(forecast))
    