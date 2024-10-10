
import requests
import json
user_input1 = input("Enter currency amount and first CCY: e.g 10000 USD: ")
currency_amount, first_ccy = user_input1.split(" ")
currency_amount = float(currency_amount)
first_ccy =str(first_ccy).upper()
print(first_ccy, currency_amount)
user_input2 = input("Enter second CCY: ")
new_url = (f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/{first_ccy}/{user_input2}")
pair_realtime_rates = requests.get(new_url)
data_2 = pair_realtime_rates.json()
print(json.dumps(data_2, indent=7))
data = data_2.get("conversion_rate")
print(data)
exchange_rate_calculated = round(currency_amount * data, 4)
print(exchange_rate_calculated)
print(f"Amount of {first_ccy.upper()}/ {user_input2.upper()}  for {currency_amount} {first_ccy.upper()}= {exchange_rate_calculated} {user_input2.upper()}")

#url_historic = (f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/historical/USD/PLN/start_date = 2012-05-01")
url = "https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/history/USD/2024/8/22"
get_url = requests.get(url)
data_historic = get_url.json()
print(json.dumps(data_historic, indent=7))
new_data = data_historic.get("conversion_rate"")
