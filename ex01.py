sum1 = 0
while True:
	choice = int(input("Enter your choice (1 or 2): "))
	if choice == 1:
		sum1 += int(input("Enter your arr num: "))
	elif choice == 2:
		break

print("The sum :", sum1)
