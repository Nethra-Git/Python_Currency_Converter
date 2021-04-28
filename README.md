# Python_Currency_Converter-
Python Project on Currency Converter 

This is a simple flask REST API in python3 that convert the provided amount​ from src_currency​ to dest_currency​, given the exchange rate at the fixer.io​
In current scope base currency is always 'EUR' and Destination currency is 'SEK'. Scope can extended for all currencies available at Fixer.io.

The api is callable like this:

	curl -X POST -H "Content-Type: application/json" -d '{"amount": 100, "src_currency": "EUR", "dest_currency": "SEK"}' http://localhost:5000/currency_converter/

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
