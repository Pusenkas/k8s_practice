# Практическая работа “Использование Kubernetes”

Задание по курсу "Облачные вычисления и виртуализация информационных ресурсов".

Структура проекта:
 - app/app.py - flask приложение. Позволяет как задавать значения, так и считывать их из redis
 - app/Dockerfile - dockerfile для flask приложения
 - db/Dockerfile - dockerfile для бд redis
 - k8s-config.yaml - конфигурационный файл, описывающий как поды flask приложения и бд redis, так и их сервисы
  

Команды:
 - minikube start                              # Запуск minikube
 - docker build -t my-flask-app:latest ./app   # Создания docker образа для flask приложения
 - docker build -t my-redis:latest -f ./db     # Создания docker образа для бд redis
 - minikube image load my-flask-app            # Сообщаем minikube о существовании
 - minikube image load my-redis                #    локальных образов
 - kubectl apply -f k8s-config.yaml            # Создаем 2 pod и 2 service с помощью конфигурационного файла
 - kubectl get pods                            # Проверяем, что 2 pod были корректно запущены (STATUS == Running)
 - minikube service flask-service --url        # Для доступа к flask приложению

Результаты:
 - Успешность запуска контейнеров можно проверить с помощью команды kubectl get pods. (pods.jpg)
 - Функционал flask-приложения можно проверить перейдя по ссылки после выполнения последней команды. (demo.mp4)
