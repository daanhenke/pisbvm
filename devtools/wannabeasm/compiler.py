import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    code = file.read()

current_operation = ""
current_argument = ""
mode = 0

for character in code:
        if character == " ":
            continue
        elif character == "\n":
            
        elif character == ",":
            mode = 1
        else:
            if mode == 0:
                current_operation += character
            elif mode == 1:
                current_argument += character
