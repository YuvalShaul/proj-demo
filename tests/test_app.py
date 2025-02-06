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
        self.assertEqual(data['operation'], 'addition')
        self.assertEqual(data['num1'], 5)
        self.assertEqual(data['num2'], 3)

    def test_add_negative_numbers(self):
        response = self.app.post('/add',
            json={'num1': -5, 'num2': 3}
        )
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], -2)

    def test_add_floating_points(self):
        response = self.app.post('/add',
            json={'num1': 5.5, 'num2': 3.3}
        )
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['result'], 8.8, places=2)

    def test_multiply_success(self):
        # Test basic multiplication
        response = self.app.post('/multiply',
            json={'num1': 5, 'num2': 3}
        )
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 15)
        self.assertEqual(data['operation'], 'multiplication')
        self.assertEqual(data['num1'], 5)
        self.assertEqual(data['num2'], 3)

    def test_multiply_by_zero(self):
        response = self.app.post('/multiply',
            json={'num1': 5, 'num2': 0}
        )
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 0)

    def test_missing_parameters(self):
        # Test missing num2
        response = self.app.post('/add',
            json={'num1': 5}
        )
        self.assertEqual(response.status_code, 400)
        
        # Test missing num1
        response = self.app.post('/multiply',
            json={'num2': 3}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_number_format(self):
        response = self.app.post('/add',
            json={'num1': 'invalid', 'num2': 3}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_json(self):
        response = self.app.post('/add',
            data='invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 500)
