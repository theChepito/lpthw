# sys.argv contains command line arguments passed to the script
from sys import argv

# uses argv to get a filename which is specified in the CL prompt.
script, filename = argv

# function open runs pydoc "open"
txt = open(filename)

# filename = name of file entered in cl prompt
print (f"Here's your file {filename}:")

# function "txt" reads contents of file
print(txt.read())

# prompts user to enter filename again
print("Type the filename again:")

# defines variable as free text input
file_again = input("> ")

# defines variable and sets function "open" to
txt_again = open(file_again)

# prints content of file
print(txt_again.read())
