from gettext import install
from locale import currency

exchange_rate = 3.81
pln_calculated = int(input("Enter amount in USD: "))
pln = pln_calculated * exchange_rate
print("Amount in PLN will be : " + str(pln))

swap_exchange_rate = (1 / exchange_rate)
usd_calculated = int(input("Enter amount in PLN: "))
usd = usd_calculated * swap_exchange_rate
print("Amount in USD will be : " + str(usd))

while True :
    ask_user = (input("Do you wish to make another exchange rate? (y/n): "))
    if ask_user == "n":
        break
    elif ask_user == "y":
        ask_curency = int(input("Do you wish to convert from usd/pln or the swap. 1 == usd/pln, 2 == pln/usd: (1/2) "))
        if ask_curency == 1:
            pln_calculated = int(input("Enter amount in USD: "))
            pln = pln_calculated * exchange_rate
            print("Amount in PLN will be : " + str(pln))
        elif ask_curency == 2:
            usd_calculated = int(input("Enter amount in PLN: "))
            usd = usd_calculated * swap_exchange_rate
            print("Amount in USD will be : " + str(usd))

#Evolution#
import requests
import json

realtime_currency = requests.get("https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/latest/USD")
data = realtime_currency.json()
print(json.dumps(data, indent=7))

rate_extracted = data["conversion_rates"]
for key, value in rate_extracted.items():
    print(f"1 USD = {value} {key}")
pln_rate_extracted = rate_extracted.get("PLN")
print(pln_rate_extracted)
new_pln_calculated = int(input("Enter amount in USD: "))
pln_1 = new_pln_calculated * rate_extracted.get("PLN")
print(f"Amount in PLN will be : {pln_1}"
      )

#evloution_2#
pair_realtime_rates = requests.get("https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/USD/NGN")
data_2 = pair_realtime_rates.json()
print(json.dumps(data_2, indent=7))

exchange_amount = int(input("Enter amount for exchange: "))
user_input1 = input("Enter first CCY: ")
user_input2 = input("Enter second CCY: ")
new_url = (f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/{user_input1}/{user_input2}")
pair_realtime_rates = requests.get(new_url)
data_2 = pair_realtime_rates.json()
print(json.dumps(data_2, indent=7))
for key, value in data_2.items():
    data_2 = value
    print(data_2)

exchange_rate_calculated = exchange_amount * data_2
print(f"Amount of {user_input1.upper()}/ {user_input2.upper()}  for {exchange_amount} {user_input1.upper()}= {exchange_rate_calculated} {user_input2.upper()}")

while True:
    ask_user = input("Do you wish to make another exchange rate? (y/n): ").lower()
    if ask_user == "n".lower():
        break
    elif ask_user == "y".lower():
        exchange_amount = int(input("Enter amount for exchange: "))
        user_input1 = input("Enter first CCY: ")
        user_input2 = input("Enter second CCY: ")
        new_url = (f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/{user_input1}/{user_input2}")
        pair_realtime_rates = requests.get(new_url)
        data_2 = pair_realtime_rates.json()
        print(json.dumps(data_2, indent=7))
        data = data_2.get("conversion_rate")
        print(data)
        exchange_rate_calculated = exchange_amount * data
        print(f"Amount of {user_input1.upper()}/ {user_input2.upper()}  for {exchange_amount} {user_input1.upper()}= {exchange_rate_calculated} {user_input2.upper()}")
#evolution 4
user_input1 = input("Enter currency amount and first CCY: e.g 10000 USD: ")
currency_amount, first_ccy = user_input1.split(" ")
currency_amount = float(currency_amount)
first_ccy =str(first_ccy).upper()
print(first_ccy, currency_amount)
user_input2 = input("Enter second CCY: ")
new_url = (f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/{first_ccy}/{user_input2}")
print(new_url)
pair_realtime_rates = requests.get(new_url)
data_2 = pair_realtime_rates.json()
print(json.dumps(data_2, indent=7))
data = data_2.get("conversion_rate")
print(data)
exchange_rate_calculated = round(currency_amount * data, 4)
print(exchange_rate_calculated)
print(f"Amount of {first_ccy.upper()}/ {user_input2.upper()}  for {currency_amount} {first_ccy.upper()}= {exchange_rate_calculated} {user_input2.upper()}")




