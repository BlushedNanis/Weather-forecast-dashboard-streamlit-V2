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
    
    return weather_data, city_data


if __name__ == "__main__":
    print(get_forecast_data("london", 2))
    