import json
import requests
from rich import print
from rich.panel import Panel
from rich import box

# ---------------------------- -- - -         WORK IN PROGRESS        - -- - ----------------------------

# ------------------------------------------  weather API  ----------------------------------------------
def weather_API():
    api_key = "0c4d43f1d3c12b565156847bb4db7717"
    
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city_names = ["Sharjah"]


    for i in city_names:
        loop_API_output = base_url + "appid=" + api_key + "&q=" + i
    
        response = requests.get(loop_API_output)
        
        x = response.json()
        
        if x["cod"] != "404":
        
            y = x['main']
        
            loop_current_temperature = y["temp"]
        
            loop_current_pressure = y["pressure"]
        
            loop_current_humidity = y["humidity"]
        
            z = x["weather"]
        
            loop_weather_description = z[0]["description"]
        
            loop_weather_info = f" [bold red]Temperature[/bold red] (in kelvin unit) = {str(loop_current_temperature)} \n [bold red]atmospheric pressure[/bold red] (in hPa unit) =  {str(loop_current_pressure)} \n [bold red]humidity[/bold red] (in percentage) =  {str(loop_current_humidity)} \n [bold red]description[/bold red] =  {str(loop_weather_description)}"
            
            return Panel(f"{loop_weather_info}", title = f"{i}", border_style = "bold white", box = box.SQUARE)
    
