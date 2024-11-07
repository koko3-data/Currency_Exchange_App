

import requests
import datetime
import csv
import json
import unittest
from unittest.mock import patch, mock_open


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


def save_result_to_file(filename, first_ccy, second_ccy, conversion_rate, currency_amount, exchange_rate_calculated):
    with open(filename, 'a') as file:
        file.write(
            f"{'Timestamp':<25}{'First Currency':<15}{'Second Currency':<15}{'Conversion Rate':<20}{'Currency Amount':<25}{'Calculated Amount':<20}\n")
        file.write(f"{'-' * 25}{'-' * 15}{'-' * 15}{'-' * 20}{'-' * 25}{'-' * 20}\n")

        # Get current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # To append
        file.write(
            f"{timestamp:<25}{first_ccy:<15}{second_ccy:<15}{conversion_rate:<20}{currency_amount:<25}{exchange_rate_calculated:<20}\n")
        print(f"Exchange result has been appended to {filename}")


def save_result_to_file_csv(filename_csv, first_ccy, second_ccy, conversion_rate, currency_amount, exchange_rate_calculated):
    with open(filename_csv, 'a', newline='') as file:  # Open file with newline=''
        writer = csv.writer(file)

        # Write header only if the file is new (not existing)
        if file.tell() == 0:  # Check if the file is empty
            writer.writerow(['Timestamp', 'First Currency', 'Second Currency', 'Conversion Rate', 'Currency Amount',
                             'Calculated Amount'])

        # Get current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # To append
        writer.writerow([timestamp, first_ccy, second_ccy, conversion_rate, currency_amount, exchange_rate_calculated])
        print(f"Exchange result has been appended to {filename_csv}")


if __name__ == "__main__":
    filename = "Currencies_Exchange_results.txt"
    filename_csv = "Currencies_Exchange_results.csv"
    while True:
        try:
            ask_user = (input("Do you wish to make an exchange? (y/n): "))
            if ask_user == "n":
                break
            elif ask_user == "y":
                user_input1 = input("Enter currency amount and first CCY: e.g 10000 USD: ")
                currency_amount, first_ccy = get_user_input(user_input1)


                user_input2 = input("Enter second CCY: ")
                second_ccy = get_user_input_2(user_input2)

                exchange_rates = get_exchange_rates(first_ccy, second_ccy)
                exchange_amount = exchange_rate_calculated(exchange_rates, currency_amount)
                formatted_result = print_result(first_ccy,second_ccy,currency_amount,exchange_amount)
                print(formatted_result)

                save_result_to_file(filename,first_ccy, second_ccy, exchange_rates, currency_amount,exchange_amount)
                save_result_to_file_csv(filename, first_ccy, second_ccy, exchange_rates, currency_amount, exchange_amount)


        except ValueError as e:
            print(f"Invalid input: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error with the request: {e}")




#unit test
class TestCurrencyExchange(unittest.TestCase):

    def test_get_user_input1(self):
        user_input1 = "1000 USD"
        currency_amount, first_ccy = get_user_input(user_input1)
        self.assertEqual(currency_amount, "1000")
        self.assertEqual(first_ccy, "USD")

    def test_get_user_input_2(self):
        user_input2 = "PLN"
        second_ccy = get_user_input_2()
        self.assertEqual(second_ccy, "EUR")

    def test_get_exchange_rates(self):
        get_exchange_rates()
        url = f"https://v6.exchangerate-api.com/v6/2d3a8f713c3474eb9c072a8f/pair/{first_ccy}/{second_ccy}"
        response = requests.get(url)
        data = response.json()
        return data.get("conversion_rate")



