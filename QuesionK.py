

#My Shop sales profit

goods1={ "cost_price": 32.00,
  "sell_price": 45.00,
  "inventory": 0}

#prompt user to enter number of sales
goods1["inventory"]=int(input("Enter number of sales:"))

#Calculate Profit (sellprice-costprice)*goods_sold aka "inventory" on the dictionary

profit=round((goods1["sell_price"]-goods1["cost_price"])*goods1["inventory"])

print(profit)

list1=list(goods1)
print(list1)