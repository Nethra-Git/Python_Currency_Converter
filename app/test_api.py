from api import currency_converter
import unittest

class TestMethods(unittest.TestCase):

    def test_negative_amount(self):
        self.assertEqual(currency_converter({'amount': -100, 'src_currency': 'EUR', 'dest_currency': 'SEK'}), {"Bad Request": "Amount should be a positive number"})
    
    def test_dest_currency(self): 
        self.assertEqual(currency_converter({'amount': 100, 'src_currency': 'EUR', 'dest_currency': 'USD'}), {"error": "Change Destination currency to SEK"})
 
    def test_src_currency(self): 
        self.assertEqual(currency_converter({'amount': 100, 'src_currency': 'SEK', 'dest_currency': 'USD'}), {"error": "Invalid input Currency, only EUR as base currency is supported for now"}) 
        
    def test_same_src_dest_currency(self): 
        self.assertEqual(currency_converter({'amount': 100, 'src_currency': 'EUR', 'dest_currency': 'EUR'}), {"error": "Invalid operation, Change Destination currency to SEK"}) 
       
if __name__ == '__main__':
    unittest.main()