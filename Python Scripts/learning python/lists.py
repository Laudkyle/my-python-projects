# Lists
numbers = [1, 2, 3, 4, 5, -1, 0, 7, 9, 10, 6]
print(numbers[0])
# Here are some methods that can be applied to lists
numbers.reverse()# Reversing the order of the list
print(numbers)
numbers.append(8)# Adding new element to the list
print(numbers)
numbers.sort()# Sorting the list out
print(numbers)
print(len(numbers))# Checking the length of a list
#numbers.clear()# Clearing the list
#print(numbers)
# Checking for the presence of an element in a list
print( 7 in numbers)
print(1 not in numbers)
# Deleting elements from list
numbers.remove(8)# Removing a particular element from the list
print(numbers)
numbers.pop()# Removing the top element
print(numbers)
del numbers[3]# Deleting using index
print(numbers)
del numbers[0:3]# Deleting a range from lists
print(numbers)