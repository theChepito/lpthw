#create a variable that holds an integer

types_of_people = 10

# create four variable that hold four strings

x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#render two strings assigned to variables x and y

print (x)
print (y)

#render two strings assigned to variables x and y

print (f"I said: {x}")
print (f"I also said: '{y}'")

#create a boolean and string variable

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#render the string variable and attach the boolean variable

print (joke_evaluation.format(hilarious))

#create two variables that hold strings

w = "This is the left side of..."
e = "A string with a right side"

#concatenate the variables w + e to form a single string

print(w + e)
