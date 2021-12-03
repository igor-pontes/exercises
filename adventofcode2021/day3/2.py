def main():
    l= None
    
    with open('input.txt', 'r') as file:
        l = [x for x in  list(file.read().split('\n')[0:-1])]
    
    
    maxcb = lambda lst: 1 if lst.count('1') > lst.count('0') or lst.count('1') == lst.count('0') else 0
    mincb = lambda lst: 0 if lst.count('1') > lst.count('0') or lst.count('1') == lst.count('0') else 1
    
    o = [x for x in l]
    c = [x for x in l]

    while(len(o) != 1):
        for y in range(0,len(l[0])):
            if(len(o) == 1):
                break
            r = []
            for x in o:
                if int(x[y]) != maxcb([x[y] for x in o]):
                    r.append(x)
        
            rmv(o, r)
   
    while(len(c) != 1):
        for y in range(0,len(l[0])):
            if(len(c) == 1):
                break
            r = []
            
            for x in c:
                if int(x[y]) != mincb([x[y] for x in c]):
                    r.append(x)
            
            rmv(c, r)

    o = int(o[0],2) 
    c = int(c[0],2)
    print(f'{o * c}')

def rmv(lst, rm):
    for x in rm:
        lst.remove(x)

main()

