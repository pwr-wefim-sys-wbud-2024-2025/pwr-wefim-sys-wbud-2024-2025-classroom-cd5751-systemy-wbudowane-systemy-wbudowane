# Stworzenie Modułu - symulacyjnego - odczyt danych środowiskowych

## Konfiguracja GitHUB Codespaces
1. Skorzystaj z codespace, z wcześniejszego modułu lub utwórz nowe: https://github.com/github/codespaces-blank
2. Add "feature"  ghcr.io/devcontainers/features/docker-outside-of-docker:1  na podstawie instrukcji:  https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces
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



