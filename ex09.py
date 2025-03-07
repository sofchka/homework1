def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

while True:
	try:
		num = int(input("Enter a number: "))
		break
	except ValueError:
		print("Invalid input.")

print(f"{num} is prime" if is_prime(num) else f"{num} is not prime")
