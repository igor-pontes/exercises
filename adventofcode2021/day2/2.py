
aim = 0

def main():
    l = None
    with open('input.txt', 'r') as file:
        l = [[x[0], int(x[1])] for x in list(map(lambda x: x.split(" "), list(file.read().split('\n')[0:-1])))]

    a = [x[1] if x[0] == "down" else -x[1] if x[0] == "up" else 0 for x in l]
    
    h = [x[1] if x[0] == "forward" else 0 for x in l ]
    
    d = [ x*aim if x != 0 else count(y) for (x,y) in zip(h, a) ]

    print(f'{sum(d)*sum(h)}')


def count(v):
   global aim
   aim = aim + v
   return 0

main()
