word = input("Write your palindrome word: ").lower()
cl_word = ""
for char in word:
	if char.isalnum(): 
		cl_word += char
if not cl_word:
	print("Invalid input.")
else:
	print("Is a palindrome" if cl_word == cl_word[::-1] else "Is not")
