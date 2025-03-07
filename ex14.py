def count(lst):
	if not isinstance(lst, list):
		print("NOT a list")
		return None
	return len(lst)

try:
	arr = input("Enter items(1 2 3): ").split()
except ValueError:
	print("invalid")
print(count(arr))
