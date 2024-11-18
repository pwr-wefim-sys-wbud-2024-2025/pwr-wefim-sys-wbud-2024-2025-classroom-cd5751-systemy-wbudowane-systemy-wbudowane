# Stworzenie Modułu - symulacyjnego - odczyt danych środowiskowych

## Konfiguracja GitHUB Codespaces
1. Skorzystaj z codespace, z wcześniejszego modułu lub utwórz nowe: https://github.com/github/codespaces-blank
2. Dodaj możliwość łączenia się z silnikiem dockerowym z terminala codespaces
    - Access the Visual Studio Code Command Palette (Shift+Command+P / Ctrl+Shift+P), then start typing "add dev". Click Codespaces: Add Dev         Container Configuration Files.
    - Wybierz z lity `modify existing configuration`
    - nazwa z rozwijanej listy `Docker  (docker-outside-of-docker) - devcontainers` < bardzo ważne
    - Domyślne paramtery są w porządku

## Python w Docker
- [Docker](https://docker-curriculum.com/#introduction)
  - Getting Started
  - Hello World
  - Webapps with Docker (bez Docker on AWS)
  - Multi Container Environments (bez AWS Elastic Container Service)
- https://code.visualstudio.com/docs/containers/quickstart-python

## Pobieranie danych pogodowych, odpalenie modułu Requestera
Cel: Stwórz moduł weather_requester, który co 30s odpytuje API Pogodowe i printuje na konsolę wiadomość.
```
{"location":<location-name>,
 "timestamp":<iso-current-time>,
"values":[
{<measurement-name>:<value> 
]}
```
Wiadomość w postaci json możesz sformatować w poniższy sposób:
```python
import json
data={....struktura powyżej....}
data_to_send=json.dumps(data)
print(data_to_send)
```
Skorzystaj z API: - Pobieranie aktualnej jakości powietrza dla wybranej lokacji z API - [https://docs.openaq.org/docs/introduction](https://docs.openaq.org/about/about)
Wymagania:
- Opakuj pobieranie danych w klasę WeatherRequester, która przyjmuje w konstruktorze lokację
- Podawaj lokację jako zmienną środowiskową
- Po przetestowaniu zamknij swój skrypt w postaci kontenera docker i uruchamiaj go z docker-compose



