#Use Arithmetic Progression !

def main(i):
    i = "input.txt" if i == 1 else "test.txt"
    crabs = None
    with open(i, 'r') as file:
        crabs = [int(x) for x in file.read().split(",")]
    fuel = float('inf')
    h = 0
    while True:
        temp = 0
        for crab in crabs:
            n = abs(crab-h)
            temp += int(n*(1+n)/2)
        if temp < fuel:
            h += 1
            fuel = temp
        else:
            break
    print(fuel)
main(1)
