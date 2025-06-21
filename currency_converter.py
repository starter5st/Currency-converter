# Simple Currency Converter

# Exchange rates (example, 1 USD to other currencies)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.15,
    "JPY": 157.50,
    "GBP": 0.78
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported."
    usd_amount = amount / exchange_rates[from_currency]
    converted_amount = usd_amount * exchange_rates[to_currency]
    return round(converted_amount, 2)

# Example usage
if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (USD, EUR, INR, JPY, GBP): ").upper()
    to_currency = input("To currency (USD, EUR, INR, JPY, GBP): ").upper()

    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result} {to_currency}")
