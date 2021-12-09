def main():
    total = 0
    signals = []
    with open('input.txt', 'r') as file:
        while(line:=file.readline()):
            temp = []
            temp.append("".join(line.split("|")[0])[0:-1].split())
            temp.append([x for x in "".join(line.split("|")[1])[0:-1].split()])
            signals.append(temp)
    
    numbers_map = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }

    for signal in signals:
        segments = {x:'' for x in char_range('a','g')} 
        signal_pattern(signal[0], segments)
        number = signal_output(signal[1], numbers_map, segments)
        total += number
    print(total)
    
def signal_output(signal, numbers_map, segments):
    number = ""
    for n in signal:
        temp = ""
        for c in n:
            for x in segments:
                if segments[x] == c:
                    temp += x
        for m in numbers_map:
            if sorted(numbers_map[m]) == sorted(temp):
                number += str(m)
    return int(number)

def signal_pattern(signal, segments):
    numbers = [0 for _ in range(10)]
    len_six = []
    len_five = []
    for s in signal:
        if len(s) == 2:
            numbers[1] = s
        if len(s) == 3:
            numbers[7] = s
        if len(s) == 4:
            numbers[4] = s
        if len(s) == 5:
            len_five.append(s)
        if len(s) == 6:
            len_six.append(s)
        if len(s) == 7:
            numbers[8] = s
    
    four_diff = set(numbers[4]).difference(set(numbers[1]))

    for n in len_six:
        if set(numbers[4]).issubset(set(n)):
            numbers[9] = n
        elif four_diff.issubset(set(n)):
            numbers[6] = n
        else:
            numbers[0] = n
    for n in len_five:
        if four_diff.issubset(set(n)):
            numbers[5] = n
        elif set(numbers[1]).issubset(set(n)):
            numbers[3] = n
        else:
            numbers[2] = n

    segments['a'] = chr(sum_bytes(numbers[7])-sum_bytes(numbers[1]))
    segments['c'] = chr(sum_bytes(numbers[8])-sum_bytes(numbers[6]))
    segments['e'] = chr(sum_bytes(numbers[8])-sum_bytes(numbers[9]))
    segments['d'] = chr(sum_bytes(numbers[8])-sum_bytes(numbers[0]))
    segments['f'] = chr(sum_bytes(numbers[1])-sum_bytes(segments['c']))
    segments['b'] = chr(sum_bytes(numbers[4]) - sum_bytes(segments['c']) - sum_bytes(segments['d']) - sum_bytes(segments['f']))
    segments['g'] = chr(sum_bytes(numbers[3]) - sum_bytes(numbers[1]) - sum_bytes(segments['a']) - sum_bytes(segments['d']))

    return segments

def char_range(a, b):
    for c in range(ord(a), ord(b)+1):
        yield chr(c)

def sum_bytes(s):
    return sum(map(ord, s))

main()

