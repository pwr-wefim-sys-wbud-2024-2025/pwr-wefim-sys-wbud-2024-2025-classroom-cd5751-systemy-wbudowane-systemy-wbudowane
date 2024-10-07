# Brokery MQTT

Opakuj kod pobierający dane z API temperaturowego i przygotuj wysyłanie na broker MQTT.
- [Tutorial MQTT - tylko wiedza o MQTT](https://cedalo.com/blog/mqtt-subscribe-publish-mosquitto-pub-sub-example/)
- [Tutorial MQTT - Biblioteka Paho](http://www.steves-internet-guide.com/mqtt/)
- [Tutorial MQTT - Biblioteka Paho v2](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python)
- Dodaj do enviroment [Biblioteka MQTT](https://pypi.org/project/paho-mqtt/)  
- Wydziel moduł wysyłania (oddzielny plik py) i opakuj go w klasę.
- [Tutorial MQTT - biblioteka paho-mqtt](https://cedalo.com/blog/configuring-paho-mqtt-python-client-with-examples/)  
- Przygotuj moduł subskrypcji, który zbiera dane od innych studentów (każdy student jest inną "lokalizacją") i zapisuje ja na dysk w postaci plików o nazwach zrobionych z topicków MQTT `("<nr-indeksy>/<lokacja>")` ma być plikewm `<nr-indeksu>-<lokacja>`
    - Wskazówka: użyj topic [Wildcards](https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/)

Dodatkowe wymagania  
- całość spakowana w kontener
- adres brokera, port podawany ze zmiennych środowiskowych
- user, hasło tak samo.
