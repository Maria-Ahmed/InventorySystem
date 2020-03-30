import stock_inventory as si

si.addProduct("Lays", 10, 50)
si.addProduct("Slanty", 5, 10)
si.addProduct("perk", 15, 5)
si.addProduct("prince", 3, 55)
si.addProduct("pepsi", 30, 500)

si.showProducts()

si.removeProduct("slanty")
si.removeProduct("prince")

print("-------------------------------")
si.showProducts()
