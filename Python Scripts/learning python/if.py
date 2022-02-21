# If statements
number = 2

if number > 0:
    print(f"number {number} is positive")
elif number == 0:
    print(f"{number} is a neither positive nor negative")
else:
    print(f" number {number} is negative")

# You can also combine if with other logical operators
if (number >4 and number < 8):
    print("number is in range")
else:
    print("number is not in range")
# Combining if with other logical operators
if not(number >4 and number < 8):
    print("number is in range")
else:
    print("number is not in range")