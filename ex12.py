while True:
	try:
		num = int(input("Enter your number: "))
		
		break
	except ValueError:
		print("Invalid!")
if num < 0:
	num *= -1
sum1 = 0
while num > 0:
	sum1 += num % 10
	num //= 10
print(sum1)
