while True:
	try:
		string = input("Input your string: ")

		print(string[::-1])
		break
	except ValueError:
		print("Invalid input. Please enter a valid integer.")
