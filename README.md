## Построение минимального микросервиса с FastApi и тесты  
Применяемые механики:  
- загрузка файла `users.json` в память сервера
- валидация данных файла при запуске сервера `uvicorn`
- обработка исключений с помощью `HTTPException`
- обработка разных типов исключений с помощью `HTTPException`
- вынос чувствительных данных в файл `.env`
- параметризация тестов `@pytest.mark.parametrize()`  
- тестирование доступности сервера через модель `AppStatus` - установка простого флага что база существует
- 