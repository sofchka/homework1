import random

attempts = 0
rand = random.randint(1, 10)

while True:
	try:
		num = int(input("Enter your guess(1-10): "))
		attempts += 1
		if 1 > num or num > 10:
			print("Wrong range")
		elif num == rand:
			print("YOU WON!!")
			break
		elif num > rand:
			print("Too high")
		else:
			print("Too low")
	except:
		print("Invalid input")

print(f"Number of your attempts: {attempts}")
