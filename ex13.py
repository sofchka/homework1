while True:
	try:
		num = int(input("Enter your number: "))

		for i in range(1,11):
			print(f"{num} * {i} = {num * i}")
		break
	except ValueError:
		print("Invalid input. Please enter a valid integer.")
