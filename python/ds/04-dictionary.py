# Dictionaries are key-value pairs that allow you to store and retrieve data based on a unique key. The
# keys must be immutable, such as strings or numbers.
# Dictionaries are useful for storing data that needs to be accessed quickly and efficiently.

product_catalog = {
'iPhone 13': 999.99,
'Samsung Galaxy S22': 849.99,
'Sony PlayStation 5': 499.99,
'MacBook Air': 1199.99,
'LG 55 inch 4K TV': 799.99
}
# Accessing the price of an iPhone 13
iphone_price = product_catalog['iPhone 13']
print(f"The price of the iPhone 13 is ${iphone_price:.2f}")
# The price of the iPhone 13 is $999.99