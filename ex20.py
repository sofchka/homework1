def gcd(n1, n2):
	if n2 == 0:
		return n1
	else:
		return gcd(n2, n1 % n2)


while True:
	try:
		n1 = int(input("Enter first number: "))
		n2 = int(input("Enter second number: "))
		if n1 == 0 and n2 == 0:
			print("Enter non-zero values.")
		else:
			print("GCD is:", gcd(n1, n2))
			break
	except ValueError:
		print("Invalid input.")




n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))





print("GCD is:", gcd(n1, n2))
