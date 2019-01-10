# JSON->XML service
Приложение запускает HTTP-сервер на локальном хосте: 8080 для обработки запросов HTTP POST с данными (строка в формате json), обеспечивая преобразование в строку формата xml.
Сервис упакован в образ докера, который построен с помощью gradle.



Чтобы создать Docker Image, нужно выполнить:                                                             

gradlew buildImage


Для запуска нужно использовать команду:                                                                               

docker run -p 8080:80 filchakova/image

Пример curl запроса:                                                                                 

curl -X POST -d '{"masha":"filchakova"}' 0.0.0.0:8080/json/to/xml/v1.0 -H "Content-Type: application/json"

Служба отправит сообщение, преобразованное в формат xml.
