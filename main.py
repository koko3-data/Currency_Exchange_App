from gettext import install

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
user_input = input("What currency would you like to convert from USD: ")
if user_input.upper() == {rate_extracted.keys}:
    print(rate_extracted.keys)
    currency_exchange = user_input.upper().rate_extracted.value
    calculated_currency = int(input("Enter amount in USD: "))
    amount = calculated_currency * currency_exchange
    print(f"Amount will be : {amount}")


