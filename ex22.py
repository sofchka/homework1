def second_largest(numbers):
	numbers = list(set(numbers))
	if len(numbers) < 2:
		return None
	numbers.sort()
	return numbers[-2]

n = int(input("Enter lenght: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter num: ")))

print("Second max: ", second_largest(arr))
