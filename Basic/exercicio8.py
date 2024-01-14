product = float(input("Product: "))
percent = float(input("Percent: "))

product = product - (product * (percent/100))

print(f"Product: R${product:5.2f}")