import itertools,timeit,re
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from operator import itemgetter
from collections import Counter
from sentence_transformers import SentenceTransformer
from txtai.embeddings import Embeddings
from txtai import graph


class ruBERT:
    def __init__(self, model_path="sergeyzh/rubert-mini-sts", content=True, functions=None, expressions=None):
        self.model_path = model_path
        self.content = content
        self.functions = [{"name": "graph", "function": "graph.attribute"},]
        self.expressions = [{"name": "category", "expression": "graph(indexid, 'category')"},
{"name": "topic", "expression": "graph(indexid, 'topic')"},]
        self.embeddings = Embeddings(path=self.model_path, content=self.content, functions=self.functions, expressions=self.expressions)

    def convert_to_embed(self, keywords):
        merged = list(itertools.chain(*keywords.values()))
        self.embeddings.index(merged)

class BERT_Process(ruBERT):
    def __init__(self, model_path="sergeyzh/rubert-mini-sts", content=True, functions=None, expressions=None):
        super().__init__(model_path, content, functions, expressions)

    def searching_embed(self, queries, sm_score):
        if sm_score > 0.99 or sm_score < 0.4:
            return None
        else:
            some_lst = []
            for query in queries:
                uid = self.embeddings.search(query, 1500)
                some_lst.extend([d['text'] if d['score'] > sm_score else None for d in uid])
            result = list(filter(lambda x: x is not None, some_lst))
            rst_without_duplicates = list(set(itertools.chain(result)))
            #print(f'without_duplicates {rst_without_duplicates}')
            return result

    def finding_element_with_and(self, test_lst):
        indexes_with_and = [i if sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('и'), x)) >= 1 else None
                            for i, x in enumerate(test_lst)]
        indexes = list(filter(lambda x: x is not None, indexes_with_and))
        if len(indexes) > 0:
            lists_with_and = itemgetter(*indexes)(test_lst)
            words = [x if x != 'и' else None for x in re.split(r'\s+', lists_with_and)]
            words = list(filter(lambda x: x is not None, words))
            return words
        else:
            return None

    def stemmer_and_regex(self, neighbors):
        stemmer = SnowballStemmer("russian")
        answer = [[stemmer.stem(word).lower() + '\w{0,}' if i < len(item.split()) - 1
                   else stemmer.stem(word).lower()
                   for i, word in enumerate(item.split())]
                  for item in neighbors]
        united_list = [(' '.join(sublist)).strip().lower() for sublist in answer]
        rst_without_duplicates = list(set(itertools.chain(united_list)))
        return rst_without_duplicates

    def creating_dict(self, rst_without_duplicates, full_dataset):
        indexes_ = []
        reviews = []
        pattern1 = r'(\w+\W+){0,5}'
        groups_counts = []
        for shablon in rst_without_duplicates:
            for index, row in full_dataset.items():
                match2 = re.search(shablon, row.lower())
                if match2:
                    indexes_.append(index)
                    groups_counts.append(shablon)
                    itog_ptrn = pattern1 + shablon + pattern1
                    regex = re.compile(itog_ptrn)
                    matches = [x.group() for x in re.finditer(regex, row.lower())]
                    matches = ','.join(matches)
                    reviews.append(matches)

        dictionary = dict(zip(indexes_, reviews))
        Counter(groups_counts)
        return dictionary
    def filter_reviews(self, dict_for_razmetka,full_dataset):
        list_by_groups = []
        for item in dict_for_razmetka.values():
            rst_without_duplicates = []
            embed_finding = self.searching_embed(item['candidates'], item['sm_score'])
            result = self.stemmer_and_regex(embed_finding)
            rst_without_duplicates.extend(list(set(itertools.chain(result))))
            print('type of full_dataset',type(full_dataset))
            result_for_one_group = self.creating_dict(rst_without_duplicates, full_dataset)
            list_by_groups.append(result_for_one_group)
        return list_by_groups

    def summarization_indexes(self, dict_for_razmetka):
        list_by_groups = []
        for item in dict_for_razmetka.values():
            rst_without_duplicates = []
            embed_finding = self.searching_embed(item['candidates'], item['sm_score'])
            result = self.stemmer_and_regex(embed_finding)
            rst_without_duplicates.extend(list(set(itertools.chain(result))))
            #list_by_groups=rst_without_duplicates ## добавил новое присвоение
            list_by_groups.append(rst_without_duplicates)#добавил новое присвоение
            #result_for_one_group = self.creating_dict(rst_without_duplicates, df)
            #list_by_groups.append(result_for_one_group) старое присвоение
        return list_by_groups

