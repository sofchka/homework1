print("Lesson 1")

# Variables

a = 100
print("The type of variable having value", a, " is ", type(a))

c = 100 + 3j			# Variable with complex value
print("The type of variable having value", c, " is ", type(c))


# Mutable
my_list = [1, 2, 3, 4]

my_list.append(5)
print(my_list)			# Output: [1, 2, 3, 4, 5]
my_list.append(5)
print(my_list)			# Output: [1, 2, 3, 4, 5, 5]

my_set = set(my_list)		# Convert list to set
print(my_set)			# Output: {1, 2, 3, 4, 5}

my_dict = {"key1": 1, "key2": 2, "key3": 3}
my_dict["key4"] = 4
print(my_dict)			# Output: {"key1": 1, "key2": 2, "key3": 3, "key4": 4}


# Immutable (different id s same variable)

my_string = "hello"
my_string[0] = "H"		# TypeError: 'str' object does not support item assignment


my_tuple = (1, 2, 3)
my_tuple[0] = 4			# TypeError: 'tuple' object does not support item assignment

name = "sofi"
print(id(name))
name = "Philipe"
print(id(name))

# Input

num = int(input("Enter valid num pls: "))
print(num);
