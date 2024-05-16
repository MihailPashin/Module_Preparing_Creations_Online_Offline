from Topics.topics_themes import dict_for_razmetka
from Topics.ECB_control_themes import Group,GroupInterface,GroupControl
from Loading_DataSet.Pandas_ECB_df import DataFrameEntity,DataFrameBoundary,DataFrameControl
from Yake_KeyWords_Extract.yake_keywords import YakeExtractor, YakeBoundary, YakeControl
from RuBERT.RuBERT_ECB import ruBERT, BERT_Process
from XLM_RoBERTa.Sentiment_Analysis_ECB import SentimentModel,SentimentModel_Process
from Nested_List_to_JSON.save_to_json import NestedListToJSON

if __name__ == "__main__" :


    group_control = GroupControl(dict_for_razmetka)
    group_interface = GroupInterface(group_control)
    group_interface.check_scores()
    group_interface.display_groups() ## Отобразил все тематики

    filepath = 'Loading_DataSet/data/New_coordinates_titles.csv'
    df_entity = DataFrameEntity(filepath)
    df_control = DataFrameControl(df_entity)
    df_control.process_data()

    df_boundary = DataFrameBoundary(df_entity)
    reviews = df_boundary.get_reviews('message') ## Получил все отзывы
    
    yake_boundary = YakeBoundary()
    keywords = yake_boundary.get_keywords(reviews) ## Проверка отзывов на словарь + KeyPhraseExtraction 
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
