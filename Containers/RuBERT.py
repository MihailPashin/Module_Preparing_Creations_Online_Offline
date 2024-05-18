from dependency_injector import containers, providers
from RuBERT.RuBERT_ECB import RuBERT_Entity,RuBERT_Boundary, RuBERT_Control

class RuBERTContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.model_path.from_value("sergeyzh/rubert-mini-sts")

    rubert_entity = providers.Factory(RuBERT_Entity, model_path=config.model_path)
    rubert_control = providers.Factory(RuBERT_Control, rubert_entity=rubert_entity)
    rubert_boundary = providers.Factory(RuBERT_Boundary, control=rubert_control)
