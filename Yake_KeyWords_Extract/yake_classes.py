from Exception.user_exception import Varierty_of_Errors
import yake

# yake_classes
class YakeExtractor:
    def __init__(self, language="ru", n=5, dedup_lim=0.65, dedup_func='seqm', window_size=1, top=15):
        self.yake_extractor = yake.KeywordExtractor(lan=language, n=n, dedupLim=dedup_lim, dedupFunc=dedup_func, windowsSize=window_size, top=top)

    def extract_keywords(self, text):
        try:
            keywords = self.yake_extractor.extract_keywords(text)
            return [keyword[0] for keyword in keywords]
        except Exception as e:
            raise Exception(f"Error extracting keywords: {e}")

class YakeBoundary:
    def validate_reviews(self, reviews):
        if not isinstance(reviews, list):
            raise ValueError("Reviews must be a list of strings")
        for review in reviews:
            if not isinstance(review, str):
                raise ValueError("Each review must be a string")

class YakeControl:
    def __init__(self):
        self.yake_extractor = YakeExtractor()

    def extract_keywords(self, reviews):
        print('Keyword extraction has started')
        keywords = []
        for review in reviews:
            keywords.extend(self.yake_extractor.extract_keywords(review))
        return keywords

