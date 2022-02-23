number = int(input("enter a number:"))
if number > 1:
	for i in range(2,number):
		if (number % 2) == 0:
			print("the number is not a prime number")
		else:
			print("the number is a prime number")
else:
	print("the number is prime number")