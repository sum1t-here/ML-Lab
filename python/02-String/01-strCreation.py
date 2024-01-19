# string creation in python

# Using single quotes
# Using double quotes
# Using triple quotes

single_quoted_string = 'Hi i am sumit'

# string concatenation
first_name = 'Sumit'
second_name = 'Mazumdar'

print(first_name+"\n\n"+second_name)

# String length
shopping_list = "Milk, Apple, Kiwi, Orange, Grapes"
items_count = len(shopping_list.split(', '))
print(f"There are {items_count} items in the shopping list")
# There are 5 items in the shopping list

latitude = "40.678.099"
langitude = "23.676.097"
lat_length = len(latitude.replace('.',' '))
long_length = len(latitude.replace('.', ' '))

print(f"Longitude has {long_length} characters and Latitude has {lat_length} characters")
# Longitude has 10 characters and Latitude has 10 characters