from Topics.topics_themes import dict_for_razmetka
from Topics.EBC_control_themes import Group,GroupInterface,GroupControl
from Loading_DataSet.Pandas_EBC_df import DataFrameEntity,DataFrameBoundary,DataFrameControl
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
    print(list_by_groups)
    print('len(list_by_groups[2]) = ',len(list_by_groups[2]))
    print('len(list_by_groups[1]) = ',len(list_by_groups[1]))
    #print(f'result from bolnichka {list_by_groups[0][0]}')
    sentiment_model = SentimentModel_Process()
    result = sentiment_model.predict_tonalnost(list_by_groups, dict_for_razmetka)
    print('Sentiment Analysis окончен. Число строк в таблице',len(result))    

    
    
    #print(f'len {len(result[0])}')
    #print(f'len {len(result[1])}')
    #print(f'len {len(result[2])}')



    #print(keywords[0:3])

    #print(reviews)
    '''       
    print(f'ready df - {dataframe_entity.df}')
    
    controller = KeywordExtractionController(reviews)
    keywords = controller.extract_keywords()
    print(f' type of keywords = {type(keywords)}')
    print(keywords[0:3])
    
    keywords = Ready_DataFrame.extract_keywords()
    print(f' type of keywords = {type(keywords)}')
    print(keywords[0:3])
    
    full_dataset = list(Ready_DataFrame.df['message'])
    #print(full_dataset[0:3])
    #print(f' type of full_dataset = {type(full_dataset)}')
    
    #word2vec_model_tiny = Word2VecModel()
    #word2vec_model_large = Word2VecModel('Word2Vec/preloaded_model/14cities.model')
    #train_tokens = word2vec_model_tiny.tokenize_corpus(full_dataset)

    result=[]

    #print(f'len {len(result)}')
    #print(f'len {len(result[0])}')
    #print(f'len {len(result[1])}')
   
    model_ruBERT = BERT_Process()
    model_ruBERT.preprocess_yake_phrases(keywords)
    print(f'Эмбединги извлечены. Активируем скрипт')    
    list_by_groups=model_ruBERT.filter_reviews(dict_for_razmetka,full_dataset)
    #print(f'result from bolnichka {list_by_groups[0][0]}')
    #print(f'result from bolnichka {list_by_groups[0]}')
    print(f'len {len(list_by_groups)}')
    print('len(list_by_groups[2]) = ',len(list_by_groups[2]))
    print('len(list_by_groups[1]) = ',len(list_by_groups[1]))
    sentiment_model = SentimentModel_Process()
    result = sentiment_model.predict_tonalnost(list_by_groups, dict_for_razmetka)
    '''
    
    #print(f'len {len(result[0])}')
    #print(f'len {len(result[1])}')
    #print(f'len {len(result[2])}')
   
