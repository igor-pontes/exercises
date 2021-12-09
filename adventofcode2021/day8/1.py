def main():
    outputs = []
    with open('input.txt', 'r') as file:
        while(line:=file.readline()):
            outputs.append("".join(line.split("|")[1])[0:-1].split())
    total = 0
    for output in outputs:
        for signal in output:
            if len(signal) == 7 or len(signal) == 4 or len(signal) == 2 or len(signal) == 3:
                total += 1
             
    print(total)


main()
