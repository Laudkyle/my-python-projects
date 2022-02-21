# Ternary if statements
number = 0
if number > 0:
    print("positive")
elif number ==0:
    print("number is neither positive nor negative")
else:
    print("negative")
# You can combine all the if statements on one line using ternary if statements
message = "positive" if number > 0 else "0 or negative"
print(message)
# Note that, the ternary if statements, you can insert only one condition