# JSON->XML service
Application starts HTTP server on localhost:8080 to process HTTP POST requests with data (json formatted string), providing converted to xml format string.
Сервис упакован в образ докера, который построен с помощью gradle.



Чтобы создать Docker Image, нужно выполнить:                                                             

gradlew buildImage


Для запуска нужно использовать команду:                                                                               

docker run -p 8080:80 {image_id}

Пример curl запроса:                                                                                 

curl -X POST -d '{"masha":"filchakova"}' 0.0.0.0:8080/json/to/xml/v1.0 -H "Content-Type: application/json"

Служба отправит сообщение, преобразованное в формат xml.
