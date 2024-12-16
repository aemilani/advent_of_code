with open('../../data/input/03.txt', 'r') as f:
    string = f.read().strip()

result = 0
for i in range(len(string)):
    try:
        if string[i:i + 4] == 'mul(':
            if string[i + 4:i + 7].isdigit():
                x = int(string[i + 4:i + 7])
                if string[i + 7] == ',':
                    if string[i + 8:i + 11].isdigit():
                        y = int(string[i + 8:i + 11])
                        if string[i + 11] == ')':
                            result += (x * y)
                    elif string[i + 8:i + 10].isdigit():
                        y = int(string[i + 8:i + 10])
                        if string[i + 10] == ')':
                            result += (x * y)
                    elif string[i + 8].isdigit():
                        y = int(string[i + 8])
                        if string[i + 9] == ')':
                            result += (x * y)
            elif string[i + 4:i + 6].isdigit():
                x = int(string[i + 4:i + 6])
                if string[i + 6] == ',':
                    if string[i + 7:i + 10].isdigit():
                        y = int(string[i + 7:i + 10])
                        if string[i + 10] == ')':
                            result += (x * y)
                    elif string[i + 7:i + 9].isdigit():
                        y = int(string[i + 7:i + 9])
                        if string[i + 9] == ')':
                            result += (x * y)
                    elif string[i + 7].isdigit():
                        y = int(string[i + 7])
                        if string[i + 8] == ')':
                            result += (x * y)
            elif string[i + 4].isdigit():
                x = int(string[i + 4])
                if string[i + 5] == ',':
                    if string[i + 6:i + 9].isdigit():
                        y = int(string[i + 6:i + 9])
                        if string[i + 9] == ')':
                            result += (x * y)
                    elif string[i + 6:i + 8].isdigit():
                        y = int(string[i + 6:i + 8])
                        if string[i + 8] == ')':
                            result += (x * y)
                    elif string[i + 6].isdigit():
                        y = int(string[i + 6])
                        if string[i + 7] == ')':
                            result += (x * y)
    except IndexError:
        pass

print(f'Part 1: {result}')

result = 0
do = True

for i in range(len(string)):
    try:
        if string[i:i + 4] == 'do()':
            do = True
        elif string[i:i + 7] == "don't()":
            do = False
    except IndexError:
        pass

    if do:
        try:
            if string[i:i + 4] == 'mul(':
                if string[i + 4:i + 7].isdigit():
                    x = int(string[i + 4:i + 7])
                    if string[i + 7] == ',':
                        if string[i + 8:i + 11].isdigit():
                            y = int(string[i + 8:i + 11])
                            if string[i + 11] == ')':
                                result += (x * y)
                        elif string[i + 8:i + 10].isdigit():
                            y = int(string[i + 8:i + 10])
                            if string[i + 10] == ')':
                                result += (x * y)
                        elif string[i + 8].isdigit():
                            y = int(string[i + 8])
                            if string[i + 9] == ')':
                                result += (x * y)
                elif string[i + 4:i + 6].isdigit():
                    x = int(string[i + 4:i + 6])
                    if string[i + 6] == ',':
                        if string[i + 7:i + 10].isdigit():
                            y = int(string[i + 7:i + 10])
                            if string[i + 10] == ')':
                                result += (x * y)
                        elif string[i + 7:i + 9].isdigit():
                            y = int(string[i + 7:i + 9])
                            if string[i + 9] == ')':
                                result += (x * y)
                        elif string[i + 7].isdigit():
                            y = int(string[i + 7])
                            if string[i + 8] == ')':
                                result += (x * y)
                elif string[i + 4].isdigit():
                    x = int(string[i + 4])
                    if string[i + 5] == ',':
                        if string[i + 6:i + 9].isdigit():
                            y = int(string[i + 6:i + 9])
                            if string[i + 9] == ')':
                                result += (x * y)
                        elif string[i + 6:i + 8].isdigit():
                            y = int(string[i + 6:i + 8])
                            if string[i + 8] == ')':
                                result += (x * y)
                        elif string[i + 6].isdigit():
                            y = int(string[i + 6])
                            if string[i + 7] == ')':
                                result += (x * y)
        except IndexError:
            pass

print(f'Part 2: {result}')
