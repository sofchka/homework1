def is_armstrong(n):
	strNum = str(n)
	lenght = len(strNum)
	res = 0
	tmp = n
	while tmp > 0:
		res += (tmp % 10) ** lenght
		tmp //= 10
	return (n == res)



num = int(input("Enter your number: "))
if is_armstrong(num):
    print("Is an Armstrong")
else:
    print("Is NOT")
