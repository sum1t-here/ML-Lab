# Sets are unordered collections of unique elements.They are useful when you need to work with distinct
# items and perform set operations like union,intersection,and difference.
# Sets are mutable, so you can add and remove elements,but the elements themselves must be
# immutable.

# create a set of favourite colors
favourite_colors = {"red", "blue", "green"}

# create an empty set for shoping items
shopping_list = set()
# add items to shopping list
shopping_list.add("apples")
shopping_list.add("banana")
shopping_list.add("milk")
print(shopping_list)
# {'apples', 'banana', 'milk'}
shopping_list.remove("milk")
print(shopping_list)
# {'apples', 'banana'}


# create sets of fruit
fruits_set1 = {"apple", "mango", "banana"}
fruits_set2 = {"watermelon", "kiwi"}
all_fruits = fruits_set1.union(fruits_set2)
print(all_fruits)
# {'watermelon', 'banana', 'kiwi', 'apple', 'mango'}


# Create an empty shopping list (analogous to an empty set)
shopping_list = set()
# Add items to your shopping list
shopping_list.add("apples")
shopping_list.add("bananas")
shopping_list.add("milk")
# Check if an item is on your list
if "apples" in shopping_list:
 print("You need to buy apples.")
else:
 print("You don't need to buy apples.")
# Remove an item from your list if you change your mind
shopping_list.discard("milk")
# Check if an item is on your list again
if "milk" in shopping_list:
 print("You need to buy milk.")
else:
 print("You don't need to buy milk.")
# Print the final shopping list
print("Your shopping list contains:", shopping_list)
# You need to buy apples.
# You don't need to buy milk.
# Your shopping list contains: {'bananas', 'apples'}
