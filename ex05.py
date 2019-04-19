name = 'Joseph'
age = 43
height = 68
weight = 174
eyes = 'blue'
teeth = 'white'
hair = 'brown'
# height_feet = round((height / 12),2)
height_inches = height % 12
height_feet = round(((height - height_inches) / 12))

print(f"Let's talk about {name}.")
print(f"He's {height_feet}'{height_inches}\" tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If i add {age}, {height}, and {weight} I get {total}.")
