import unittest
from main import analyze_attributes


class TestAnalyzeAttributes(unittest.TestCase):

    def test_string_attribute(self):
        data = {"key": "value"}
        schema = analyze_attributes(data)
        expected_schema = {
            "key": {
                "tag": "",
                "description": "",
                "required": False,
                "type": "string"
            }
        }
        self.assertEqual(schema, expected_schema)

    def test_integer_attribute(self):
        data = {"key": 42}
        schema = analyze_attributes(data)
        expected_schema = {
            "key": {
                "tag": "",
                "description": "",
                "required": False,
                "type": "integer"
            }
        }
        self.assertEqual(schema, expected_schema)

    def test_enum_attribute(self):
        data = {"key": ["value1", "value2"]}
        schema = analyze_attributes(data)
        expected_schema = {
            "key": {
                "tag": "",
                "description": "",
                "required": False,
                "type": "enum"
            }
        }
        self.assertEqual(schema, expected_schema)

    def test_array_of_object_attribute(self):
        data = {"key": [{"key1": "value1"}, {"key1": "value1"}]}
        schema = analyze_attributes(data)
        expected_schema = {
            "key": {
                "tag": "",
                "description": "",
                "required": False,
                "type": "array",
            }
        }
        self.assertEqual(schema, expected_schema)

if __name__ == '__main__':
    unittest.main()
