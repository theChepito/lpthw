# end= '' tells print to stay on the same line, not to add \n character

# the input() function stops program flow until user provides given input and
# presses return key. The text of the input will be printed on the screen
# the input of the user will be returned as a string

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()


print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
