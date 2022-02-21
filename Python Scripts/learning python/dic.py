dic1={
    "name1": "value1",
    "name2": "value2",
    "name3": "value3",
    "name4": "value1",
    "name5": "value3"
}
with open("application_list.txt", "a") as f:
    for key in dic1:
        content = f"{key},{dic1[key]} \n"
        f.write(content)
dic2 = {}
with open("application_list.txt", 'r') as file:
    for line in file:
        dicline = line.split(',')
        key = dicline[0]
        value = dicline[1].replace(' \n', '')
        dic2[key] = value
print(dic2)
print(dic1)

