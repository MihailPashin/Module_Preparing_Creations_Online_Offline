import torch,pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class SentimentModel:
    def __init__(self, model_name="sismetanin/xlm_roberta_base-ru-sentiment-rureviews"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, return_dict=True)

    def predict(self, text):
        tokens = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**tokens)
            probabilities = torch.nn.functional.softmax(outputs.logits, dim=1)
            predicted = torch.argmax(probabilities).item()
            max_probability = torch.max(probabilities).item()
        return predicted, max_probability

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
                predicted, max_probability = self.predict(text)
                indexes_reviews.append(idx)
                tonalty_class.append(self.tonality_labels[predicted])
                weights.append(max_probability)
                print(f'item - {text}, tonalty_class {self.tonality_labels[predicted]} ')

            temp_df = pd.DataFrame({'Индекс': indexes_reviews,
                                    'Оценка': tonalty_class,
                                    'Вес прогноза': weights})
            temp_df['Group'] = group_value
            result = pd.concat([result, temp_df], ignore_index=True)

        result['Вес прогноза'] = result['Вес прогноза'] * result['Оценка'].apply(
            lambda x: 1 if x == 'Положительная' else (-1 if x == 'Негативная' else 0)
        )
        return result

