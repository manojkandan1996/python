from forex_python.converter import CurrencyRates

def convert_currency():
    c = CurrencyRates()
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., INR): ").upper()

    try:
        result = c.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        print("Error:", e)

convert_currency()