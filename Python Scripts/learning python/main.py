# Dictionarys

person = {
    "name": "Kyle",
    "age": 22,
    "country" : "Ghana"
}

print(person["name"], "is from", person["country"])
print(person.keys())
print(person.values())
print(person)
#person.clear()
print(person.get("age"))# Updating the values of a dictionary
person['age'] = 100
print(person)


# Dictionaries are used to define properties of an object