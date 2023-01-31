import unittest
import requests

class ClassifyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/api/classify"

    def test_classify(self):
        # Sample pixels data
        pixels = [0 for i in range(754)]
        data = {'pixels': pixels}

        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['classification'], 'expected_result')

if __name__ == '__main__':
    unittest.main()
