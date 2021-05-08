print("Hello")

name = "World"
print(name)

message = "Hello " + name + "!"  # String concatenation.
print(message)

print(name[0])  # Print first letter.
print(name[2])  # Print third letter.
print(len(name))  # Length of name (integer).
print(name[1:])  # Substring from letter 2 to end. "orld"
print(name[2:4])  # Substring from 3rd to 4th letter. "rl"

word1 = "Hello"
word2 = "World"

message = "Y" + word1[1:5] + "w " + word2 + "!"
print(message)
