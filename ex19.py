vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0

while True:
    word = input("Enter your word: ")
    if word.strip() == "":
        print("Please enter a valid word.")
    else:
        for letter in word:
            if letter in vowels:
                count += 1
        print(f"Number of vowels: {count}")
	break
