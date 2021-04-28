#!#Python Project on Currency Converter 

#Import neccessary modules required

#The datetime module supplies classes for manipulating dates and times.
#Flask  is the prototype used to create instances of web application
#Library allow you to send HTTP/1.1 requests 


from datetime import datetime

from flask import Flask, abort, request
import requests
import json

app = Flask(__name__)


@app.route("/currency_converter/", methods=['POST'])
# Main method to automate the currency conversion process
def currency_converter(data = None):

    url = "http://data.fixer.io/api/latest?access_key=e893e2e8622b73546983d793c7af3643&symbols=SEK"
    resp = requests.get(url)
    
    if not data:
        data = request.json
        
    currency_src = data["src_currency"]
    currency_dest = data["dest_currency"]
    amount = data["amount"]
      
     # Convert user I/O Currency to Upper string        
    currency_dest = currency_dest.upper().strip()
       
    currency_src = currency_src.upper().strip()

    # Currency list is limited to 2 currencies as per requirement
    currency_list = ["EUR","SEK"]

    #Type casting amount to Float
    amount = float(amount)
    
    # Validation to make sure all entries are valid
    if amount <= 0:
        return {"Bad Request": "Amount should be a positive number greater than zero, please enter again the amount"}

    data = resp.json()
    # To convert unix timestamp string to readable date time 
    dt_string = datetime.fromtimestamp(
        int(data['timestamp'])).strftime('%d-%m-%Y %H:%M:%S')

    # Validation to make sure all entries are valid
    if resp.status_code != 200:
        return {"error": "Remote API Server Error"}, resp.status_code
    
    if currency_src == currency_dest:
        return {"error": "Invalid operation, Change Destination currency"}
        
    if currency_src != 'EUR':
        return {"error": "Invalid input Currency, only EUR as base currency is supported for now"}

    if currency_dest and currency_dest not in data['rates']:
        return {"error": "Invalid Output Currency"}    

    elif currency_dest:

        return {
            "input": {
                "amount": amount,
                "Currency 1": currency_src,
                "Currency 2": currency_dest,
            },

            "output": {
                "time": dt_string,
                "from": currency_src,
                "to": currency_dest,
                "amount": amount,
                "rate": data['rates'][currency_dest] ,
                "converted_result": round(data['rates'][
                    currency_dest] * amount, 2),
            }
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)