import requests
import json 
from json import loads
import os
import time

# odczyt zmiennych 
lokalizacja = os.getenv("location",None)

# definicja klasy Weather Requests
class WeatherRequester:
    def __init__(self, lokalizacje):
        self.lokalizacja
    
    def loop(self):
        while True:
            url = "..................."
            r = requests.get(url)
            if r.status_code == 200:
                msg = r.json()
                print(msg)
                mqtt_client.publish()
                #coś robimy z msg
            time.sleep(30)

# Tworzymy obiekt klasy
weather_requester = WeatherRequester(lokalizacja)

# Wywołujemy f-cje dla danego obiektu
weather_requester.loop()


