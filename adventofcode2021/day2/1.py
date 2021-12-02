def main():
    l = None
    with open('input.txt', 'r') as file:
        l = [[x[0], int(x[1])] for x in list(map(lambda x: x.split(" "), list(file.read().split('\n')[0:-1])))]
    
    h = sum([x[1] for x in l if x[0] == "forward"])
    d = sum([x[1] if x[0] == "down" else -x[1] if x[0] == "up" else 0 for x in l])
    print(f'{d*h}') 
main()
