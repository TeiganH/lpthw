# imports argv from sys
from sys import argv

# the arguments are script and filename
script, filename = argv

# opening the filename is assigned to the txt variable
txt = open(filename)

# print the name of the filename
print(f"Here's your file {filename}:")
# print the content of the txt varialbe
print(txt.read())

print asking for file name again
print("Type the filename again:")
#assign an input request with > to prompt to the variable file_again
file_again = input("> ")

# open the file_again variable and assign it to the varialbe txt_again
txt_again = open(file_again)

#print the contents of the txt_again variable
print(txt_again.read())

txt.close()
txt_again.close()
