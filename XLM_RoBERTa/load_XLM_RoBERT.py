import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class SentimentModel:
    def __init__(self, model_name="sismetanin/xlm_roberta_base-ru-sentiment-rureviews"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, return_dict=True)
