import json 

class NestedListToJSON:
    def __init__(self, nested_list):
        self.nested_list = nested_list
    
    def save_to_json(self, folder_name, jsons):
        try:
            with open("{}/{}.json".format(folder_name,jsons), 'w',encoding='utf-8') as json_file:
                json.dump(self.nested_list, json_file, ensure_ascii=False)
        except Exception as e:
            print(f"An error occurred: {e}")
