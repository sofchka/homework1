def fibonacci(n):
    if n < 0: 
        print("Invalid input!")
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_print(n):
	for i in range(n):
        	print(fibonacci(i), end = " ")
	
n = int(input("Enter: "))
fibonacci_print(n)
