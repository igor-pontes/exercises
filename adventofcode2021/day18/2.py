from math import ceil, floor
def main():
    numbers = []
    values = []
    with open('input.txt', 'r') as file:
        while line := file.readline()[:-1]:
            numbers.append(substitute(line))  
    i = 1
    largest = 0
    for key1, n1 in enumerate(numbers):
        for key2, n2 in enumerate(numbers):
            if n1 == n2:
                continue
            value = join(numbers[key1], numbers[key2])
            changes = True
            while changes:
                changes, value = calculate(value, 0, 0)
            temp = magnitude(value)
            if temp > largest:
                largest = temp

    print(largest)

def magnitude(number):
    total = 0
    have_numbers = True
    while have_numbers:
        have_numbers = False
        lst = []
        for key, n in enumerate(number):
            if n == "[":
                if is_number(number, key):
                    have_numbers = True
                    lst = number[:key] + [str(int(int(number[key+1])*3 + int(number[key+3])*2))] + number[key+5:]
                    if len(lst) == 1:
                        total = int(lst[0])
                        break
        number = lst
    return total 

def substitute(number):
    index = 0
    n = []
    while index < len(number):
        temp = check_numerical(number, index, [])
        if temp[0] is not None:
            n.append(temp[0])
            index = temp[1]
        else:
            n.append(number[index])
            index += 1
    return n

def check_numerical(number, index, temp):
    if number[index].isnumeric():
        temp.append(number[index])
        r = check_numerical(number, index+1, temp)
        return ("".join(temp), r[1])
    else:
        return (None, index)

def count_opens(number, index):
    o = 0
    i = 0
    while i < len(number[:index]):
        if number[i] == "[":
            o += 1
        if number[i] == "]":
            o -= 1
        i += 1
    return o

def calculate(number, changes, index):
    if number[index] == "[":
        if is_number(number, index):
            if count_opens(number, index) == 4:
                add_left(number, index+1)
                add_right(number, index+3)
                number[index] = "0"
                index -= 1
                for _ in range(2, 6):
                    number.pop(index+2)
                changes = True
            changes, number = calculate(number, changes, index+1)
        else:
            changes, number = calculate(number, changes, index+1)
    else:
        if number[index] == "]":
            if index == len(number)-1:
                return changes, number
        if number[index].isdigit():
            if int(number[index]) >= 10 and not changes:
                n = ["["]
                n.append(str(floor(int(number[index])/2)))
                n.append(",")
                n.append(str(ceil(int(number[index])/2)))
                n.append("]")
                lst = number[:index] + n + number[index+1:]
                number = lst
                changes = True
        changes, number = calculate(number, changes, index+1)
    return changes, number

def add_left(number, index):
    n = number[index]
    i = index
    while i >= 0:
        i -= 1
        if number[i].isdigit():
            number[i] = str(int(number[i])+int(n))
            return True
    number[index] = 0
    return False

def add_right(number, index):
    n = number[index]
    i = index
    while i < len(number)-1:
        i += 1
        if number[i].isdigit():
            number[i] = str(int(number[i])+int(n))
            return True
    number[index] = 0
    return False

def is_number(number, index):
    temp = []
    while number[index] != "]":
        temp.append(number[index])
        index += 1
    index += 1
    if temp.count("[") != 1: 
        return False
    else:
        return True

def join(number1, number2):
    return substitute("[" + "".join(number1) + "," + "".join(number2) + "]")

main()
