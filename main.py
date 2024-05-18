from Containers.Yake import Yake_Container
from Containers.Topic_Checker import Topic_Container
from Containers.DF_Pandas import Pandas_Container
from Containers.RuBERT import RuBERT_Container
from Containers.XLM_RoBERTa import SentimentModel_Container
from Containers.List2JSON import Save2JSON_Container
import pandas as pd

if __name__ == "__main__" :
   
    topic_boundary = Topic_Container().boundary()
    topics=topic_boundary.check_groups_and_save() ## Отобразил и вернул все тематики
    print('Выполнено сохранение тематик')

    df_boundary = Pandas_Container().boundary()
    reviews = df_boundary.get_reviews('message')  # Получил все отзывы  
    entire_df = df_boundary.get_all_dataframe()   # Получил весь датафрейм
    print('Импотированный датасет сохранен и приведен к нужному формату - ', type(entire_df))
    
    yake_boundary = Yake_Container().boundary()
    keywords = yake_boundary.get_keywords(reviews) ## Проверка отзывов на словарь + Извлечение ключ. фраз.
    print('Ключевые фразы извлечены и приведены к формату ', type(keywords))
    container = Save2JSON_Container()
    container.config.nested_list.from_value(keywords)
    container.init_convert().save_to_json('yake_keywords.json') ## Сохрание ключ. фраз в JSON 

    rubert_boundary = RuBERT_Container().boundary()
    rubert_boundary.activate_embed(keywords) # Создание векторного пространства слов.
    list_by_groups = rubert_boundary.process_reviews(topics, reviews)
    print('Разметка отзывов по тематикам выполнена и сохранена ')
    
    sentiment_boundary = SentimentModel_Container().boundary()
    result = sentiment_boundary.analyze_sentiments(list_by_groups, topics)
    print('Sentiment Analysis произведён. Число строк в таблице',len(result))
    sliced_df = pd.concat([result.head(5), result.tail(5)])
    print ('Результирующий DataFrame',sliced_df)


