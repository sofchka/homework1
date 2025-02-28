while True:
	try:
		choice = int(input("Choose 1 => +   2 => -   3 => *   4 => /   5 => EXIT: "))
		if choice == 5:
			break
		num1 = int(input("first number: "))
		num2 = int(input("second number: "))
		match choice:
			case 1:
				print(num1 + num2, "\n")
			case 2:
				print(num1 - num2, "\n")
			case 3:
				print(num1 * num2, "\n")
			case 4:
				if (num2 == 0):
					print("num cant be divided by 0!!")
				else:
					print(num1 / num2, "\n")
			case _:
				print("INVALID num choice!")
	except:
		print("Invalid input")
