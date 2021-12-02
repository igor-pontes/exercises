def main():
    l = None
    with open('input.txt', 'r') as file:
        l = list(map(int, file.read().split('\n')[0:-1]))

    l = [sum([l[x], l[x+1], l[x+2]]) for x in range(0, len(l[0:-2]))]
    
    y = [float("inf")]
    y.extend(l[0:-1])

    l = len([x for x, y in zip(l, y) if x > y])

    print(f'{l}') 
main()
