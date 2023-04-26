# SberTech_PPPRP

Приложение состоит из двух микросервисов: nginx как reverse proxy и приложение на Flask, которое ходит в публичное API [numbersapi.com](http://numbersapi.com/#42). Сслылки на образы: [nginx](https://hub.docker.com/r/karinakonopleva/nginx_alpine) и [flask](https://hub.docker.com/r/karinakonopleva/flask). По ручке ```/numberinfo/{number}``` приложение отдает информацию о числе ```number```. Пример запроса и ответа:

```bash
karina@MacBook-Pro-Karina istio-1.17.2 % curl 127.0.0.1/numberinfo/3
3 is the number of sets needed to be won to win the whole match in volleyball.
```

### Запуск приложения
Поставьте istio
``` bash
curl -L https://git.io/getLatestIstio | sh -
```

Добавьте ```bin/``` из получившейся директории в path

Запустите minikube
```bash
minikube start --memory 4096

```
И в отдельном окне откройте туннель
```bash
minikube tunnel
```
Сделайте файл ```start.sh``` исполняемым
```bash
chmod +x start.sh
```
И запустите скрипт - он применит все yaml-файлы
```bash
./start.sh
```
Можно отправлять запросы вида `http://127.0.0.1/numberinfo/{number}`
