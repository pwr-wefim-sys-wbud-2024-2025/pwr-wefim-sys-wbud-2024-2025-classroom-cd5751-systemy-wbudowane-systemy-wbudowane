# Stworzenie Modułu - symulacyjnego - odczyt danych środowiskowych

## Konfiguracja GitHUB Codespaces
1. Skorzystaj z codespace, z wcześniejszego modułu lub utwórz nowe: https://github.com/github/codespaces-blank
2. Add "feature"  ghcr.io/devcontainers/features/docker-outside-of-docker:1  na podstawie instrukcji:  https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces
  - nazwa z rozwijanej listy **Docker  (docker-outside-of-docker) - devcontainers** < bardzo ważne

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

Wymagania:
- Opakuj pobieranie danych w klasę WeatherRequester, która przyjmuje w konstruktorze lokację
- Podawaj lokację jako zmienną środowiskową
- Po przetestowaniu zamknij swój skrypt w postaci kontenera docker i uruchamiaj go z docker-compose

Możesz użyć przykładowej konfiguracji debugowania (folder `.vscode`) oraz docker stąd:
- Konfiguracja CodeSpaces: https://github.com/bpasz/codespaces-project-template-py
- Konfiguracje są w folderze `DataRequstor` `cd DataRequestor/`
- Komenda do odpalania z folderu `DataRequester` jest taka: `docker compose -f docker-compose.debug.yml up`
- Pobieranie aktualnej jakości powietrza dla wybranej lokacji z API - https://docs.openaq.org/docs/introduction
- Wysyłanie danych z lokacji po MQTT

# Poniżej archiwum
## Siemens S7 Data Blocks
- [Co to są DBs](https://www.automation.siemens.com/sce-static/learning-training-documents/classic/advanced-programming/b04-data-blocks-en.pdf)
- [Wstęp do biblioteki Snap7](https://snap7.sourceforge.net/) > dział Snap7 Package/ Overview
- [Pobierz wersję `1.4.2`](https://sourceforge.net/projects/snap7/files/1.4.2/snap7-full-1.4.2.7z/download)



## Symulator PLC

1. Stwórz dockerfile z apką Python
2. Instalacja zarówno w ramach pliku Docker, jak i środowiska wirtualnego [python-snap7)](https://python-snap7.readthedocs.io/en/latest/)
3. Stworzenie serwera symulującego Simens DataBlock https://python-snap7.readthedocs.io/en/latest/API/server.html
   1. DB100
   2. 10 x string (100 znaków max lenght)
   3. 2 x 8 bool
   4. Struktura EnvMeasurement x 20
      1. String - nazwa pomiaru
      2. Real - wartość
      3. Real - timestamp pomiaru
   5. Wpisywane są co 5s przypadkowe wartości
4. Potwierdzenie za pomocą klienta z 1.4.2 działania serwera
5. Pobieranie aktualnej jakości powietrza dla wybranej lokacji z API - https://docs.openaq.org/docs/introduction
   1. wpisywanie do data blocku do struktury EnvMeasurement odczytanych wartości
   
