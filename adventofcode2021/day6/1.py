def main(days):
    total = 0
    fishes = None
    with open("input.txt", "r") as file:
        fishes = [int(x) for x in list(file.read())[0:-1] if x != ","]
    fishes = [fishes.count(i) for i in range(9)]
    
    for _ in range(days):
        fishes = iterate_fishes(fishes)
    for f in range(len(fishes)):
        total += fishes[f]
    print(total)

def iterate_fishes(fishes):
    temp_fishes = [0 for _ in fishes]
    temp_fishes[8] += fishes[0]
    temp_fishes[6] += fishes[0]
    
    for f in range(1,len(fishes)):
        temp_fishes[f-1] += fishes[f]
    return temp_fishes
main(256)
