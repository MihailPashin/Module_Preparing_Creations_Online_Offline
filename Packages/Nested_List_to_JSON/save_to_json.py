import json 

class NestedListToJSON:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def save_to_json(self, file_path):
        try:
            with open(file_path, 'w',encoding='utf-8') as json_file:
                json.dump(self.nested_list, json_file, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")
