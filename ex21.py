def is_armstrong(n):
	length = len(str(n))
	res = 0
	tmp = n
	while tmp > 0:
		res += (tmp % 10) ** length
		tmp //= 10
	return n == res


while True:
	try:
		num = int(input("Enter your number: "))
		break
	except ValueError:
		print("invalid!")

if is_armstrong(num):
	print("Is an Armstrong")
else:
	print("Is NOT")

