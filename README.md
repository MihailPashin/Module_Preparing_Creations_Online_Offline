
# Модуль подготовки критериев на Python. С применением нейросетевой обработки отзывов.  

## Цель - 
**обработать отзывы по запросу "новостройки" с сайта yandex.ru/maps и присвоить каждому району степень привлекательности**

## Задачи:
    1. Предобработать датасет. В каталоге Loading_DataSet есит Class DataProcessor и скрипт для запуска Ready_DataFrame.
    2. Подгрузка тем. Каталог Topics содержит Topics
    3. RuBERT-2 + TxtAI. Поиск схожих векторных представлений фраз для распознавания тем. В каталоге RuBERT хранятся классы ruBERT, BERT_Process(ruBERT).
    4. Отбор отзывов по поисковым шаблонам из предыдущего шага.  

## Результат сравнения- Лепестковая диаграмма по семи группам

Развертывания модуля локально: 

1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python3 main&#46;py

Запуск модуля в Google Colab: 
[ссылка на код](https://colab.research.google.com/drive/1RdSNP5cAV2ZQGXLf6vxykboap8o2hJTD?usp=sharing)

