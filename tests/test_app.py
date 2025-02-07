import unittest
import json
from src.app import app

class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_add_success(self):
        # Test basic addition
        response = self.app.post('/add',
            json={'num1': 5, 'num2': 3}
        )
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 8)

   
    def test_multiply_success(self):
        # Test basic multiplication
        response = self.app.post('/multiply',
            json={'num1': 5, 'num2': 3}
        )
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 15)

   
if __name__ == '__main__':
    unittest.main()