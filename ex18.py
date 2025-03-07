arr = []
for i in range(3):
	while True:
		try:
			num = int(input("Enter num: "))
			arr.append(num)
			break
		except ValueError:
			print("Invalid input!")

print("max is", max(arr))
