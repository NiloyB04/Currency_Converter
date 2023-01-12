from forex_python.converter import CurrencyRates

c = CurrencyRates()

print("Welcome to this currency conversion tool!\nYou will have the opportunity to convert between two currencies and choose how much you want to convert.")
print("Here is a list codes of some popular currencies: ")
popular_currencies = ["USD", "EUR", "GBP", "HKD", "JPN", "CNY", "CAD", "INR" ]
print(popular_currencies)


# Get user input for the currencies they want to convert from and to
from_c = input("Enter the currency you want to convert from: ")
to_c = input("Enter the currency you want to convert to: ")
amount = float(input("Enter the amount you want to convert: "))

# Get the current exchange rate between the user-specified currencies
rate = c.get_rate(from_c, to_c)

# Use the exchange rate to convert the user-specified amount
result = c.convert(from_c, to_c, amount)

print(f'{amount} {from_c} converts to {result} {to_c}')
