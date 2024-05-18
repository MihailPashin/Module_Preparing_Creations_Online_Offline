import unittest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Containers.List2JSON import Save2JSON_Container

class TestNestedListToJSON(unittest.TestCase):
    
    def setUp(self):
        self.json_saver = Save2JSON_Container()

    def test_simple_nested_list(self):
        nested_list = [1, [2, 3], [[4, 5], 6]]
        expected_json = [1, [2, 3], [[4, 5], 6]]        

        self.json_saver.config.nested_list.from_value(nested_list)
        self.json_saver.init_convert().save_to_json('Results_in_JSON','test.json')

        with open(f"Results_in_JSON/test.json", 'r', encoding='utf-8') as json_file:
            actual_json = json.load(json_file)

        self.assertEqual(expected_json,actual_json)

    def test_list_of_dictionaries(self):
        nested_list = [{"name": "John", "age": 25}, {"name": "Alice", "age": 30}]
        expected_json = [{"name": "John", "age": 25}, {"name": "Alice", "age": 30}]
        self.json_saver.config.nested_list.from_value(nested_list)
        self.json_saver.init_convert().save_to_json('Results_in_JSON','test2.json')

        with open(f"Results_in_JSON/test2.json", 'r', encoding='utf-8') as json_file:
            actual_json = json.load(json_file)

        self.assertEqual(expected_json, actual_json)

if __name__ == '__main__':
    unittest.main()
