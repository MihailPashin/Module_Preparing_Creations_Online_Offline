from Topics.ECB_control_themes import Group,GroupInterface,GroupControl
from Loading_DataSet.Pandas_ECB_df import DataFrameEntity,DataFrameBoundary,DataFrameControl
from Yake_KeyWords_Extract.yake import YakeExtractor, YakeBoundary, YakeControl
from RuBERT.RuBERT_ECB import RuBERT_Entity,RuBERT_Boundary, RuBERT_Control
from XLM_RoBERTa.Sentiment_Analysis_ECB import SentimentModel_Entity,SentimentModel_Boundary,SentimentModel_Control
from Nested_List_to_JSON.save_to_json import NestedListToJSON
from Preparing_Tables.Grouping_Summary import DataProcessor, DataBoundary, DataController
import pandas as pd
from Containers.Yake import Yake_Container
from Containers.Topic_Checker import Topic_Container
from Containers.DF_Pandas import Pandas_Container

if __name__ == "__main__" :
     
    topic_boundary = Topic_Container().group_boundary()
    topic_boundary.display_groups()
    topic_boundary.check_scores() ## Отобразил все тематики   
    
    container = Pandas_Container()
    container.config.filepath.from_value('Loading_DataSet/data/New_coordinates_titles.csv')
    df_boundary = container.dataframe_boundary()
    df_boundary.controller.process_data()
    reviews = df_boundary.get_reviews('message')  # Получил все отзывы
    entire_df = df_boundary.get_all_dataframe()   # Получил весь датафрейм
    print(f' Тип данных переменной result - ', {type(entire_df)})
    print(f' Число строк result - ', {len(entire_df)})

    yake_boundary = Yake_Container().boundary()
    keywords = yake_boundary.get_keywords(reviews) ## Проверка отзывов на словарь + KeyPhraseExtraction.
    print(f' Тип данных переменной keywords = ', {type(keywords)} )
    print(f' Число строк result - ', {len(keywords)})
    '''
    yake_boundary = YakeBoundary()
    keywords = yake_boundary.get_keywords(reviews) ## Проверка отзывов на словарь + KeyPhraseExtraction.
    print(f' Тип данных переменной keywords = ', {type(keywords)} )
    print(f' Число строк result - ', {len(keywords)})
   
    rubert_boundary = RuBERT_Boundary()
    rubert_boundary.activate_embed(keywords)
    list_by_groups = rubert_boundary.process_reviews(dict_for_razmetka, reviews)
    print(f'len {len(list_by_groups)}')
    print('len(list_by_groups[2]) = ',len(list_by_groups[2]))
    print('len(list_by_groups[1]) = ',len(list_by_groups[1]))

    sentiment_boundary = SentimentModel_Boundary()
    result = sentiment_boundary.analyze_sentiments(list_by_groups, dict_for_razmetka)
    print('Sentiment Analysis окончен. Число строк в таблице', len(result))    
    print(f' Тип данных переменной result - ', {type(result)})

    sliced_df = result.head(5)
    sliced_df = pd.concat([sliced_df, result.tail(5)])

    print ('resulting_dataframe',sliced_df)
    #converter = NestedListToJSON(list_by_groups) ## Сохранение в JSON формат для теста
    #converter.save_to_json('nested_list_yake.json')

    

    data_processor = DataProcessor()
    data_controller = DataController(data_processor)
    data_boundary = DataBoundary(data_controller)
    all_dataset = df_boundary.get_all_dataframe()
    df_entity.display_info()
    processed_data = data_boundary.validate_and_process(result, all_dataset)
    sliced_df = processed_data.head(5)
    sliced_df = pd.concat([sliced_df, processed_data.tail(5)])
    print('Транспонированная таблица', sliced_df)
    '''

    
    #user = DataBoundary()
    #user.validate_and_process()
