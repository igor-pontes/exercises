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
            steps = 0
            for c in range(0, abs(h-crab)+1):
                steps += c
            temp += steps
        if temp < fuel:
            h += 1
            fuel = temp
        else:
            break
    print(fuel)
main(1)
