def factorial(n):
	if n < 0:
		print("Invalid Input!!")
		return None
	elif n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

print(factorial(-11))
