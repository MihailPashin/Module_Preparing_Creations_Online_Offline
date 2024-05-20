
# Модуль подготовки критериев на Python. С применением нейросетевой обработки отзывов.  

## Цель - 
**обработать отзывы по запросу "новостройки" с сайта yandex.ru/maps и присвоить каждому району степень привлекательности**

## Задачи:
    1. Предобработать датасет. Class DataProcessor и скрипт для запуска Ready_DataFrame.
    2. Подгрузка тем. Каталог Topics содержит Topics
    3. Языковая модель RuBERT-2 + TxtAI. Поиск схожих векторных представлений фраз для распознавания тем.
    4. Отбор отзывов по поисковым шаблонам из предыдущего шага.  
    5. Проведение оценки тональности благодаря языковой модели XLM-RoBERTa
    6. Сохранение всех таблиц в JSON для последующей загрузки в БД   

## Способы развертывания

Развертывания модуля с помощью Docker-Hub [ссылка](https://hub.docker.com/repository/docker/mikhailpaskhinkgu/neurallanguagesmethods/general): 

1. Вы в директории --> 
2. mkdir output Создаём папку в bash терминале
3. sudo docker run --rm --name mycontainer -v "$(pwd)/output:/output" mikhailpaskhinkgu/neurallanguagesmethods . Команда для открытия контейнера  
4. Ожидаем выполнение скрипта и загрузку в папке output JSON файлы. Они источник данных для MySQL

Развертывания модуля локально: 

1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python3 main&#46;py

Запуск модуля в Google Colab: [ссылка на код](https://colab.research.google.com/drive/1RdSNP5cAV2ZQGXLf6vxykboap8o2hJTD?usp=sharing)

