import torch,timeit,pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from XLM_RoBERTa.load_XLM_RoBERT import SentimentModel

class SentimentModel_Process(SentimentModel):
    def __init__(self, model_name="sismetanin/xlm_roberta_base-ru-sentiment-rureviews"):
        super().__init__(model_name)
        self.tonality_labels = {0: "Нейтральная", 1: "Негативная", 2: "Положительная"}

    def predict_tonalnost(self, dictionary, name_groups):
        result = pd.DataFrame(columns=['Индекс', 'Оценка', 'Вес прогноза', 'Group'])
        for k, s in enumerate(dictionary):
            tonalty_class = []
            weights = []
            indexes_reviews = []
            group_value = name_groups[k]['name_group']

            for idx, text in s.items():
                predicted = super().predict(text)
                indexes_reviews.append(idx)
                tonalty_class.append(self.tonality_labels[predicted])
                weights.append(torch.max(self.model.forward(text).probabilities).item())

            temp_df = pd.DataFrame({'Индекс': indexes_reviews,
                                    'Оценка': tonalty_class,
                                    'Вес прогноза': weights})
            temp_df['Group'] = group_value
            result = pd.concat([result, temp_df], ignore_index=True)

        result['Вес прогноза'] = result['Вес прогноза'] * result['Оценка'].apply(
            lambda x: 1 if x == 'Положительная' else (-1 if x == 'Негативная' else 0)
        )
        return result
