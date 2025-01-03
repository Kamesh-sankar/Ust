items=["bread","Cookies","Butter","Cheese","Yoghurt"]
price=[40,80,120,180,60]
new_items=[]
print(items)
while(True):
  print("What do you want to do?")
  print("Enter 1  for Viewing the items in the cart")
  print("Enter 2  Adding an item to the cart")
  print("Enter 3  Updating the items from the cart")
  print("Enter 4  Deleting an item from the cart")
  print("Enter 5 for printing the bill")
  choice=int(input("Enter your choice:"))
  if choice == 1:
    for i in range(len(items)):
      print(f"Name :{items[i]} and Price :{price[i]}")
  elif choice == 2:
    i=input("Enter the item name:")
    if i in items:
      quantity = int(input("Enter the quantity: "))
      index = items.index(i)
      item_price = price[index]
      total_price = item_price * quantity
      new_items.append([i, quantity, item_price, total_price])
      print(f" added to the cart.")
  elif choice == 3:
    item_name=input("Enter the item name to update:")
    if item in new_items:
      if item[0] == item_name:
                new_quantity = int(input("Enter the quantity to be updated: "))
                item[1] = new_quantity
                item[3] = item[2] * new_quantity
                print(f"{item_name} updated in the cart.")
                break
  elif choice == 4:
    item_name=input("Enter the item name to delete:")
    for item in new_items:
      if item[0] == item_name:
          new_items.remove(item)
          print(f"{item_name} removed from the cart.")
          break
  elif choice == 5:
    print("\nCart Details:")
    print("Name\tQuantity\tPrice\tTotal")
    total = 0
    for item in new_items:
      print(f"{item[0]} {item[1]}  {item[2]}  {item[3]}")
      total += item[3]
      print(f"Total Amount of Bill: {total_amount}")
  elif choice == 6:
    break