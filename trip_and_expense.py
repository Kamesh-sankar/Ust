def TripCost(km,liters,price):
  return km*liters*price
def ExpenseCalculation(quantity,price):
  cost=quantity*price
  if quantity>10:
    cost=cost*0.9
  return cost
kilometers=float(input("Enter the kilometers to drive:"))
liters=float(input("Enter the liters per kilometer usage :"))
price=float(input("Enter the price of fuel per liter:"))
print("The cost of the trip is:",TripCost(kilometers,liters,price))

quantity=int(input("Enter the quantity of the item:"))
price=float(input("Enter the price of the item:"))
print("The cost of the item is:",ExpenseCalculation(quantity,price))