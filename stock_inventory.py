products = []


def addProduct(name, price, qty):
    products.append({"name": name, "price": price, "qty": qty})


def showProducts():
    for p in products:
        print(
            f"Name: {p['name']} - Price: {p['price']} - Quantity: {p['qty']}")


def removeProduct(name):
    for p in products:
        if p["name"].lower() == name.lower():
            products.remove(p)
            break
#Enhance stock inventory module. Make functions for (1) Increment and Decrement quantity. (2) Rename product name. (3) Change product price.
