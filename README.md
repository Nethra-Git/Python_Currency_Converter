# Python_Currency_Converter
**Python Project on Currency Converter **

This is a simple flask REST API in python3 that convert the provided amount​ from src_currency​ to dest_currency​, given the exchange rate at the fixer.io​
In current scope base currency is always 'EUR' and Destination currency is 'SEK'. Scope can be extended for all currencies available at Fixer.io.

**Requirements**

	Python => 3
	flask
	json
	pytest 

**Run the Flask App**

	$ python3 app/api.py

The api is callable like this:

	$ curl -X POST -H "Content-Type: application/json" -d '{"amount": 100, "src_currency": "EUR", "dest_currency": "SEK"}' http://localhost:5000/currency_converter/

The response is a JSON object like:

	{
  	"input": {
    "Currency 1": "EUR", 
    "Currency 2": "SEK", 
    "amount": 100.0
  	}, 
  	"output": {
    "amount": 100.0, 
    "converted_result": 1011.74, 
    "from": "EUR", 
    "rate": 10.117429, 
    "time": "28-04-2021 11:04:04", 
    "to": "SEK"
  	}
	}
	
**To run unittest on API**

	$ pytest app/test_api.py -v or pyhton3 app/test_api.py -v
	
The response should be like below:

	=================================test session starts===============================================

	platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
	cachedir: .pytest_cache
	collected 4 items                                                                                                                                                                                         

	test_api.py::TestMethods::test_dest_currency PASSED                                                                                                                                                 [ 25%]
	test_api.py::TestMethods::test_negative_amount PASSED                                                                                                                                               [ 50%]
	test_api.py::TestMethods::test_same_src_dest_currency PASSED                                                                                                                                        [ 75%]
	test_api.py::TestMethods::test_src_currency PASSED                                                                                                                                                  [100%]
	================================= 4 passed in 1.19s===================================================

	
