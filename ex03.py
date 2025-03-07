def calculator(argument):
	parentheses = 0
	for char in argument:
		if char == "(":
			parentheses += 1
		elif char == ")":
			parentheses -= 1
	
	if parentheses != 0:
		print("Invalid parentheses")
		return
	else:
		for char in argument:
			if char.isdigit() == False and char not in "*+-/()":
				argument = argument.replace(char, "")
	try:
		result = eval(argument)
		print(result)
	except:
		print("Invalid mathematical expression")


test_cases = [
	"2 + 2",
	"3 * (4 + 1)",
	"5 - 3 / 2",
	"7 * (2 + 3)",
	"3 + (2 * 5)",
	"(3 + 2",
	"3 + 2)",
	"((5 + 1)",
	"aaa + 3",
	"2 + $ + 5",
	"3 + @",
	"foo + 3",
	"",
	"3 +",
	"2 *",
	"5 + (",
	"(",
	"3 + a * 2",
	"5 + (3 * foo)",
	"9(3 + 2)",		# only case that doesn't have Error handling
	"3 / (2 + 1",
	"3 + 4 * ",
]

for test in test_cases:
	print(f"Testing: {test}")
	calculator(test)
	print("---")
