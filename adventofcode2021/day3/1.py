def main():
    lst = None
    
    with open('input.txt', 'r') as file:
        lst = [x for x in  list(file.read().split('\n')[0:-1])]
    
    maxcb = lambda lst: max(((x, lst.count(x)) for x in set(lst)), key = lambda a: a[1])[0]
    mincb = lambda lst: min(((x, lst.count(x)) for x in set(lst)), key = lambda a: a[1])[0]

    g = int("".join([maxcb([x[y] for x in lst]) for y in range(0,len(lst[0]))]), 2)

    e = int("".join([mincb([x[y] for x in lst]) for y in range(0,len(lst[0]))]), 2)

    print(f'{g*e}')

main()

