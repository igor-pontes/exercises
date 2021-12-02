def main():
    l = None
    with open('input.txt', 'r') as file:
        l = list(map(int, file.read().split('\n')[0:-1]))
    y = [float("inf")]
    y.extend(l[0:-1])
    l = len([x for x, y in zip(l, y) if x > y])
    print(f'{l}') 
main()


