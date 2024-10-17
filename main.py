
import requests
import json

from main_2v import ask_user
def get_user_input(user_input1):
    currency_amount, first_ccy = user_input1.split(" ")
    return float(currency_amount), first_ccy.upper()

def get_user_input_2(second_ccy):
    return second_ccy.upper()

def get_exchange_rates(first_ccy, second_ccy):
    url = f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/{first_ccy}/{second_ccy}"
    response = requests.get(url)
    data = response.json()
    return data.get("conversion_rate")

def exchange_rate_calculated(data, currency_amount):
    return round(currency_amount * data, 4)

def print_result(first_ccy,second_ccy,exchange_rate_calculated,currency_amount):
    return print(f"Amount of {first_ccy.upper()}/ {second_ccy.upper()}  for {currency_amount} {first_ccy.upper()}= {exchange_rate_calculated} {second_ccy.upper()}")

if __name__ == "__main__":
    try:
        user_input1 = input("Enter currency amount and first CCY: e.g 10000 USD: ")
        currency_amount, first_ccy = get_user_input(user_input1)


        user_input2 = input("Enter second CCY: ")
        second_ccy = get_user_input_2(user_input2)

        exchange_rates = get_exchange_rates(first_ccy, second_ccy)
        exchange_amount = exchange_rate_calculated(exchange_rates, currency_amount)
        print_result(first_ccy,second_ccy,exchange_rates,currency_amount)

    except ValueError as e:
        print(f"Invalid input: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error with the request: {e}")