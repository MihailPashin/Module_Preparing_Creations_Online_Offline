from dependency_injector import containers, providers
from XLM_RoBERTa.Sentiment_Analysis_ECB import SentimentModel_Entity,SentimentModel_Boundary,SentimentModel_Control

class SentimentModel_Container(containers.DeclarativeContainer):
    
    group_control = providers.Factory(GroupControl, data=topics_data)
    group_boundary = providers.Factory(GroupInterface, control=group_control)
