stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 320}

total_investment = 0
portfolio = []

print("Available Stocks:", stock_prices)

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        portfolio.append((stock, quantity, investment))

        print(f"{stock} added. Investment = ${investment}")

    else:
        print("Stock not found!")

print("\nYour Portfolio:")
for item in portfolio:
    print(item[0], "Quantity:", item[1], "Value: $", item[2])

print("Total Investment = $", total_investment)


file = open("portfolio.txt", "w")
file.write("Stock Portfolio\n")

for item in portfolio:
    file.write(f"{item[0]}  Qty:{item[1]}  Value:${item[2]}\n")

file.write(f"Total Investment = ${total_investment}")
file.close()

print("\nPortfolio saved to portfolio.txt")
