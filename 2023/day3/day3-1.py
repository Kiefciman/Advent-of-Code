input = open("input.txt", "r")

digits = []
symbols = []
numbers = []
engineparts = []
sum = 0
used_digits = []

for linenum, line in enumerate(input):
    digits_in_line = []
    line  = line.rstrip()
    for charpos, char in enumerate(line):
        if char != ".":
            if char.isdigit():
                digits_in_line.append([char, charpos, linenum])
            else:
                symbols.append([char, charpos, linenum])
    digits.append(digits_in_line)

for digits_in_line in digits:
    for digit1 in digits_in_line:
        for digit2 in digits_in_line:
            for digit3 in digits_in_line:
                if digit1[1] == digit2[1] + 1:
                    if digit2[1] == digit3[1] + 1:
                        newnum = [digit3[0] + digit2[0] + digit1[0], [digit3[1], digit2[1], digit1[1]], digit1[2]]
                        if digit3 not in used_digits:
                            if digit2 not in used_digits:
                                if digit1 not in used_digits:
                                    numbers.append(newnum)
                                    used_digits.append(digit3)
                                    used_digits.append(digit2)
                                    used_digits.append(digit1)
                                    #print(newnum)

for digits_in_line in digits:
    for digit1 in digits_in_line:
        for digit2 in digits_in_line:
            if digit1[1] == digit2[1] + 1:
                newnum = [digit2[0] + digit1[0], [digit2[1], digit1[1]], digit1[2]]
                if digit2 not in used_digits:
                    if digit1 not in used_digits:
                        numbers.append(newnum)
                        used_digits.append(digit2)
                        used_digits.append(digit1)
                        #print(newnum)

for digits_in_line in digits:
    for digit1 in digits_in_line:
        newnum = [digit1[0], [digit1[1]], digit1[2]]
        if digit1 not in used_digits:
            numbers.append(newnum)
            used_digits.append(digit1)
            #print(newnum)

for number in numbers:
    for symbol in symbols:
        if number[2] == symbol[2]:
            if number[1][0] == symbol[1] + 1:
                if number not in engineparts:
                    engineparts.append(number)
            elif number[1][len(number[1]) - 1] == symbol[1] - 1:
                if number not in engineparts:
                    engineparts.append(number)
        elif number[2] == symbol[2] + 1:
            if number[1][0] - 1 <= symbol[1]:
                if number[1][len(number[1]) - 1] + 1 >= symbol[1]:
                    if number not in engineparts:
                        engineparts.append(number)
        elif number[2] == symbol[2] - 1:
            if number[1][0] - 1 <= symbol[1]:
                if number[1][len(number[1]) - 1] + 1 >= symbol[1]:
                    if number not in engineparts:
                        engineparts.append(number)

for enginepart in engineparts:
    sum += int(enginepart[0])

print(sum)
#print(engineparts)
#for enginepart in engineparts:
#    print(enginepart)
#for digit in digits:
#    print(digits)
#print(digits[0])
#for number in numbers:
#    print(number)
#print(used_digits)
