from Topics.topics_themes import dict_for_razmetka
from Topics.ECB_control_themes import Group,GroupInterface,GroupControl
from Loading_DataSet.Pandas_ECB_df import DataFrameEntity,DataFrameBoundary,DataFrameControl
from Yake_KeyWords_Extract.yake_keywords import YakeExtractor, YakeBoundary, YakeControl
from RuBERT.RuBERT_ECB import ruBERT, BERT_Process
from XLM_RoBERTa.Sentiment_Analysis_ECB import SentimentModel,SentimentModel_Process
from Nested_List_to_JSON.save_to_json import NestedListToJSON
from Preparing_Tables.Grouping_Summary import DataProcessor, DataBoundary, DataController
import pandas as pd

if __name__ == "__main__" :


    group_control = GroupControl(dict_for_razmetka)
    group_interface = GroupInterface(group_control)
    group_interface.check_scores()
    group_interface.display_groups() ## Отобразил все тематики

    filepath = 'Loading_DataSet/data/New_coordinates_titles.csv'
    df_boundary = DataFrameBoundary(filepath)
    df_boundary.controller.process_data()
    reviews = df_boundary.get_reviews('message')
    entire_df = df_boundary.get_all_dataframe()
    print(f' Тип данных переменной result - ', {type(entire_df)})
    print(f' Число строк result - ', {len(entire_df)})
    '''
    df_boundary = DataFrameBoundary(df_entity)
    reviews = df_boundary.get_reviews('message') ## Получил все отзывы. Верно - актор может общаться с интерфейсом
    
    yake_boundary = YakeBoundary()
    keywords = yake_boundary.get_keywords(reviews) ## Проверка отзывов на словарь + KeyPhraseExtraction. - актор может общаться с интерфейсом
    print(f' type of keywords = {type(keywords)}', len(keywords))
    
    #converter = NestedListToJSON(keywords) ## Сохранение в JSON формат для теста
    #converter.save_to_json('nested_list.json')
    
    bert_processor = BERT_Process()
    bert_processor.convert_to_embed(keywords)
    print(f'Эмбединги извлечены. Активируем скрипт')
    list_by_groups = bert_processor.filter_reviews(dict_for_razmetka, reviews)
    print(f'len {len(list_by_groups)}')
    print('len(list_by_groups[2]) = ',len(list_by_groups[2]))
    print('len(list_by_groups[1]) = ',len(list_by_groups[1]))
    #print(f'result from bolnichka {list_by_groups[0][0]}')
    sentiment_model = SentimentModel_Process()
    result = sentiment_model.predict_tonalnost(list_by_groups, dict_for_razmetka)
    print('Sentiment Analysis окончен. Число строк в таблице', len(result))    
    print(f' Тип данных переменной result - ', {type(result)})

    sliced_df = result.head(5)
    sliced_df = pd.concat([sliced_df, result.tail(5)])

    print ('resulting_dataframe',sliced_df)
    
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
