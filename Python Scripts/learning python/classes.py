# Creating Classes
class Phone:
	
	def __init__(self, brand, price):
		self.brand = brand
		self.price = price
	def __str__(self) -> str:
		return f"Brand {self.brand}\n Price {self.price}"
iphone = Phone("Iphone", 400)
sumsung= Phone("Sumsung", 400)

print(iphone)
print(sumsung)
iphone.brand="dert"
print(iphone)