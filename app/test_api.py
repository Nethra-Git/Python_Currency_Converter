## Script to test currency_converter api

from api import currency_converter
import unittest
import requests

class TestMethods(unittest.TestCase):

    def test_negative_amount(self):
        self.assertEqual(currency_converter({'amount': -100, 'src_currency': 'EUR', 'dest_currency': 'SEK'}), {"Bad Request": "Amount should be a positive number"})
    
    def test_dest_currency(self): 
        self.assertEqual(currency_converter({'amount': 100, 'src_currency': 'EUR', 'dest_currency': 'USD'}), {"error": "Change Destination currency to SEK"})
 
    def test_src_currency(self): 
        self.assertEqual(currency_converter({'amount': 100, 'src_currency': 'SEK', 'dest_currency': 'USD'}), {"error": "Invalid input Currency, only EUR as base currency is supported for now"}) 
        
    def test_same_src_dest_currency(self): 
        self.assertEqual(currency_converter({'amount': 100, 'src_currency': 'EUR', 'dest_currency': 'EUR'}), {"error": "Invalid operation, Change Destination currency to SEK"})
        
    def test_url_response_code_equals_200(self):
        url = "http://data.fixer.io/api/latest?access_key=e893e2e8622b73546983d793c7af3643&symbols=SEK"
        resp = requests.get(url)
        assert resp.status_code == 200
        
    def test_base_currency_equals_EUR(self):
        url = "http://data.fixer.io/api/latest?access_key=e893e2e8622b73546983d793c7af3643&symbols=SEK"
        resp = requests.get(url)
        data = resp.json()
        assert data['base'] == 'EUR'   

    def test_target_currency_list_equals_one(self):
        url = "http://data.fixer.io/api/latest?access_key=e893e2e8622b73546983d793c7af3643&symbols=SEK"
        resp = requests.get(url)
        data = resp.json()
        assert len(data['rates'])== 1    
       
if __name__ == '__main__':
    unittest.main()
