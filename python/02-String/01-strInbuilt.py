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

# Accessing characters

#  You can access individual characters within a string in Python using indexing, which is 0-based.
#  The first character is at index 0, the second at index 1, and so on.
#  You can also use slicing to extract a range of characters from a string.

names = ["Iron man", "Ct. America", "Hulk"]
first_letters = [name[0] for name in names]
print(first_letters)
# ['I', 'C', 'H']

# extract username from email before @
email="mazumdarsumit3@gmail.com"
username=email[:email.index('@')]
print(username)
# mazumdarsumit3

# seperate domain
url = "https://www.PWIOI.com/blog/article"
domain = url[8:url.index('/', 8)]
# start slicing from from https:// (i.e 8) till first slash after 8 ('/', 8)

#Analogy: In natural language processing, you may need
# to identify and extract specific phrases or words from a
# sentence.
sentence = "Machine learning is fascinating."
word1 = sentence[0:7] # "Machine"
word2 = sentence[20:31] # "fascinating"
print(word1, word2)

#Analogy: In a text processing application, you might
# want to extract the initial letter of a sentence.
sentence = "Python is a versatile programming language."
first_char = sentence[0]
print("first character is :",first_char)