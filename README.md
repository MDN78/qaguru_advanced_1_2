## Построение минимального микросервиса с FastApi и тесты  
Применяемые механики:  
- загрузка файла `users.json` в память сервера
- валидация данных файла при запуске сервера `uvicorn`
- обработка исключений с помощью `HTTPException`
- обработка разных типов исключений с помощью `HTTPException`
- вынос чувствительных данных в файл `.env`
- параметризация тестов `@pytest.mark.parametrize()`  
- тестирование доступности сервера через модель `AppStatus` - установка простого флага, что база существует
- Использование библиотеки `fastapi-pagination` для базовой пагинации в эндпоинтах  
[fastapi-pagination](https://github.com/uriyyo/fastapi-pagination)  


### Задание:  
1. Расширить тестовое покрытие smoke тестами на доступность микросервиса.
2. Добавить сервисный эндпоинт /status для проверки доступности микросервиса.
3. Использовать библиотеку fastapi-pagination для базовой пагинации в эндпоинтах, которые возвращают список объектов.
4. Добавить тесты на пагинацию. Тестовых данных должно быть достаточно для проверки пагинации (не менее 10).
5. Проверяем:
    - ожидаемое количество объектов в ответе;
    - правильное количество страниц при разных значениях size;
    - возвращаются разные данные при разных значениях page;

## Доработаем микросервис - добавим базу данных  
1. Добавим реализацию базы данных (docker + postgres)
2. Обновим тесты  
Новые библиотеки в проекте:  
- `psycopg2-binary` - драйвер для работы с базой данных postgres  
- `sqlalchemy` 
- `sqlmodel` - позволяет использовать стандартные модели pydantic для описания моделей из базы данных

3. Получим с `docker hub` необходимый конфигурационный файл  `docker-compose.yml` и поместим в проект  
[docker hub](https://hub.docker.com/_/postgres)
4. Запустить Docker локально `C:\Program Files\Docker\Docker\Docker Desktop.exe`  
<details><summary>Docker container local</summary>
<br>
<img src="assets/docker_container.PNG">
</details>

5. Запуск командой 
```commandline
docker compose up -d
```

и перейти по адресу порта `http://localhost:8080/` и убедится что админка из файла `docker-compose.yml` активна  

<details><summary>Adminer</summary>
<br>
<img src="assets/adminer.PNG">
</details>

Можем войти используя имя/пароль из docker файла: `Use postgres/example user/password credentials`  
<details><summary>Database</summary>
<br>
<img src="assets/database.PNG">
</details>


6. Остановка удаление запущенного контейнера Docker коммандой
```commandline
docker compose down
```
7. Добавить возможность доступа к базе данных извне, добавив в файл `docker-compose.yml` необходимую информацию  
```html
    ports:
      - 5432:5432
```
Данные будут храниться:
```html
volumes:
  db-data:
```
8. Прописать строку для доступа к базе данные sqlalchemy в env файле:  
`DATABASE_ENGINE=postgresql+psycopg2://postgres:example@localhost:5432/postgres`
9. 
