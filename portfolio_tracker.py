filename = "portfolio_summary.txt"

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
}

portfolio = {}
total_value = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️ Stock not in list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("⚠️ Quantity cannot be negative.")
            continue
    except ValueError:
        print("⚠️ Invalid quantity. Please enter a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

save = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()
if save == "yes":
    try:
        with open(filename, "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("========================\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_value}")
        print(f"✅ Portfolio saved to '{filename}'.")
    except PermissionError:
        print("❌ Unable to save the file due to permission issues.")