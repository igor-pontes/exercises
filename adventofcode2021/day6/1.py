def main(days):
    fishes = None
    with open("input.txt", "r") as file:
        fishes = [int(x) for x in list(file.read())[0:-1] if x != ","]
    day = 0
    while day < days:
        for f in range(len(fishes)):
            fishes[f] -= 1
        temp = fishes.count(-1) 
        if temp > 0:
            for k, f in enumerate(fishes):
                if fishes[k] == -1:
                    fishes[k] = 6
        for _ in range(temp):
            fishes.append(8)
        day += 1
    print(len(fishes)) 

main(80)
