import unittest
import requests

class ClassifyTestCase(unittest.TestCase):
    
    def create_app(self):
        return app

    def test_classify(self):
        # Sample pixels data
        pixels = [0 for i in range(784)]
        data = {'pixels': pixels}

        response = requests.post("http://localhost:5000/classify", json=data)
        expected_result = {"class": '0'}

        assert result == expected_result, f"Expected {expected_result} but got {result}"
        print("Test passed!")

if __name__ == '__main__':
    unittest.main()
