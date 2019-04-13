# \t indents the string a single tab space
tabby_cat = "\t\tI'm tabbed in."

# \n drops the subsequent portion of the string onto a new line
persian_cat = "I'm split\non a line"

# the first \ escapes the second \ so the second \ becomes part of the string
backslash_cat = "I'm \\ a \\ cat."


# """ recognizes all intentional new lines as separate lines. Include \t for indention
# and \n to create new line
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("here are some escape functions:")

print("Backslash \\")
print("Single-quote \'")
print("Double-quote \"")
print("ASCII \a bell")
print("ASCII \b backspace")
print("ASCII \f formfeed")
print("ASCII \n linefeed")
#print("Character named name in Unicode database \N{name}")
print("Carriage \r Return")
print("Horizontal \t Tab")
#print("Character with 16-bit hex value xxxx") \uxxxx
#print("Character with 32-bit hex value xxxxxxxxx \Uxxxxxxxx")
print("ASCII vertical \v Tab")
#print("Character with octal value ooo \ooo")
#print("Character with hex value hh \xhh")
