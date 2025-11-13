# 🟢 Stock Portfolio Tracker
# Goal: Calculate total investment using predefined stock prices

# dictionary with stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total_investment = 0  # variable to store total amount

print("Welcome to Stock Portfolio Tracker!")
print("Enter 'done' when you finish.\n")

while True:
    stock = input("Enter stock symbol (AAPL/TSLA/GOOG): ").upper()

    if stock == 'DONE':
        break  # exit the loop when done

    if stock in stocks:
        qty = int(input(f"Enter quantity of {stock}: "))
        total_investment += stocks[stock] * qty
    else:
        print("Invalid stock symbol. Please try again.")

# show total investment
print(f"\n💰 Total Investment Value: ${total_investment}")
