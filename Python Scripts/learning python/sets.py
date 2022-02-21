"""
SETS
Sets are the same as list except that sets so not print dulplicate
The methods that are used for lists can be used for sets too.
There is no order to the arrangement of sets
"""
numberlist = [1, 1, 2, 3]
numberset = {1, 1, 2, 3}
lettersSet = {"A", "A", "B", "C", "D"}
print(numberlist)
print(numberset)
print(lettersSet)
print()

"""
You can perform set operations such as UNION AND INTERSERTION on sets
"""
print(" SET OPERATIONS")
print()
lettersA ={"A", "B", "D"}
lettersB ={"C", "F", "A"}

#Union of sets
print(lettersA | lettersB)

# Intersection
print(lettersA & lettersB)

# Difference or Compliment
print(lettersA - lettersB)
print(lettersB - lettersA)
