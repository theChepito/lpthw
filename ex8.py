# define the variable formatter to contain four functions
formatter = "{} {} {} {}"

# pass the four functions defined in the variable formatter, four int arguments
print(formatter.format(1, 2, 3, 4))

# pass the four functions defined in the variable formatter, four string arguments
print(formatter.format("one", "two", "three", "four"))

# pass the four functions defined in the variable formatter, four boolean arguments
print(formatter.format(True, False, False, True))

# pass the four functions defined in the variable formatter, four variable arguments
print(formatter.format(formatter, formatter, formatter, formatter))

# pass the four functions defined in the variable formatter, four string arguments
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
