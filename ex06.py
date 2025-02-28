word = input("Write your palindrome word: ").lower()

print("Is a palindrome" if word == word[::-1] else "Is not")
