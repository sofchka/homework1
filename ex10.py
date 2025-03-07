def fibonacci(n):
	if n < 0:
		return None
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	
	a, b = 0, 1
	for _ in range(2, n + 1):
		a, b = b, a + b
	return b

def print_fib(n):
	for i in range(n):
        	print(fibonacci(i), end = " ")
	
while True:
	try:
		n = int(input("Enter: "))
		if n < 0:
			print("Non-negative!")
		else:
			break
	except ValueError:
		print("Invalid input!")

print_fib(n)
