# slice operator

fruits = ["apples", "pear", "oranges"]
text = "Hello, I like python"

print(fruits[1]) # prints "pear"
print(text[1]) # prints "e"

print(text[0:5]) # prints "Hello"
print(text[:5])  # prints starting from the beginning
print(text[2:])  # prints "Hello, I like python"

# step feature
print(text[::2]) # steps every other letter
print(text[::3]) # steps every third letter

print(text[3::3]) # steps from the fourth letter and steps by three

print(fruits[1:])

# insert function

# fruits.append("bananas") # appends to the end of the list

fruits[2:2] = "b"
print(fruits)