# implementation of Array

arr = [ 2,1,4,5,6,8,9 ]

#random access

print(arr[4]) ## 6

## Search for an element '15' and if it's present in the array
## return the index else return -1

x = 15

def linearSearch(arr,x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    return -1

# time complexity = O(N)
# space complexity = O(1)

result = linearSearch(arr, x)
print("15 is present at index ", result) # 15 is present at index  -1


## Insert an element 5 at index 2
arr.insert(2, 5)
print(arr) # [2, 1, 5, 4, 5, 6, 8, 9]

#time complexity = O(N)

## Remove an element from the orginal array
arr.remove(8)
print(arr) # [2, 1, 5, 4, 5, 6, 9]

## count the number of elements
print(arr.count(5)) # 2

## Delete an element in a particular index
arr.pop(4)
print(arr) # [2, 1, 5, 4, 6, 9]

arr.sort()
print(arr) # [1, 2, 4, 5, 6, 9]

## Extract the index of any given element
print(arr.index(5)) # 3

## Reverse an array
arr.reverse()
print(arr) # [9, 6, 5, 4, 2, 1]
