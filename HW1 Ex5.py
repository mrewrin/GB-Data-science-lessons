profit = float(input("Enter the company's revenue "))
costs = float(input("Enter the firm's costs "))
if profit > costs:
    print(f"The company is operating at a profit. Return on revenue amounted to {profit / costs:.2f}")
    workers = int(input("Enter the number of company employees: "))
    print(f"Profit per employee was {profit / workers:.2f}")
elif profit == costs:
    print("The company is running at zero.")
else:
    print("The company is operating at a loss.")