def calculate_emi(principal, annual_rate, tenure_years):
    r = annual_rate / (12 * 100)  # Monthly interest rate
    n = tenure_years * 12         # Total number of payments
    emi = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return emi, n

def generate_schedule(principal, annual_rate, tenure_years):
    emi, n = calculate_emi(principal, annual_rate, tenure_years)
    balance = principal

    print(f"\nMonthly EMI: ₹{emi:.2f}\n")
    print(f"{'Month':<6}{'EMI':<12}{'Interest':<12}{'Principal':<12}{'Balance'}")
    print("-" * 55)

    for month in range(1, int(n)+1):
        interest = balance * (annual_rate / (12 * 100))
        principal_paid = emi - interest
        balance -= principal_paid
        print(f"{month:<6}{emi:<12.2f}{interest:<12.2f}{principal_paid:<12.2f}{max(balance, 0):.2f}")

# Example usage
generate_schedule(principal=500000, annual_rate=8.5, tenure_years=5)