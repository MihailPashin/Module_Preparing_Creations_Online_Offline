from Exception.user_exception import Varierty_of_Errors

class Group:
    def __init__(self, name_group, candidates, sm_score):
        self.name_group = name_group
        self.candidates = candidates
        self.sm_score = sm_score

    def is_sm_score_valid(self):
        return 0.66 < self.sm_score < 0.99

class GroupInterface:
    def __init__(self, control):
        self.control = control

    def display_groups(self):
        groups = self.control.get_groups()
        for idx, group in groups.items():
            print(f"Тематика отзывов {idx+1}: {group.name_group}")

    def check_scores(self):
        for idx, group in self.control.get_groups().items():
            if not(group.is_sm_score_valid()):
                raise Varierty_of_Errors(f"Тематика отзывов {idx}: {group.name_group} с невалидным sm_score: {group.sm_score}. Диапазон допустимых значений 0.66 < x < 0.99")
    

class GroupControl:
    def __init__(self, data):
        self.groups = {}
        self.load_data(data)

    def load_data(self, data):
        for idx, info in data.items():
            if self.validate_entry(info):
                self.groups[idx] = Group(info['name_group'], info['candidates'], info['sm_score'])
            else:
                print(f"Некорректный ввод {idx}")

    def validate_entry(self, info):
        required_keys = {'name_group', 'candidates', 'sm_score'}
        if not required_keys.issubset(info.keys()):
            return False
        if not isinstance(info['candidates'], list) or not all(isinstance(candidate, str) for candidate in info['candidates']):
            return False
        if not isinstance(info['sm_score'], (int, float)):
            return False
        return True

    def get_groups(self):
        return self.groups
