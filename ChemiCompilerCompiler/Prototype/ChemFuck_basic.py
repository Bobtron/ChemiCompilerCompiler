
"""
This is a basic version of a chemical equation -> ChemFuck translation

What it does, is given a list of sx, tx, ax, (additional ptr destination), and action @ # $
It will generate the chemfuck needed. This chemfuck is after all the values for the pointers
have been generated (i.e. you will need to do shit like >+>++>+++>++++ etc. to set the
values at the each of the available ptr destinations. So all the program has to do
is to go to the preset values at each pointer and set them to the registers as necessary.

The program assumes you are starting at ptr = 0, so you will have to do a series of <<<<<<... after
creating

"""

steps = []
ptr = 0

with open('input_regs.txt', 'r') as file:
    for line in file.readlines():
        steps.append(line[:-1].split())

print(steps)

regs = ['}', ')', "'"]

for step in steps:
    string = ''
    for i in range(len(step) - 1):
        dest = int(step[i])
        if ptr < dest:
            string += '>' * (dest - ptr)
            ptr = dest
        else:
            string += '<' * (ptr - dest)
            ptr = dest
        if i < len(regs):
            string += regs[i]
    string += step[-1]
    print(string)

print('~')
