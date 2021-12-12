counter = 0
caves = [] 
def main():
    global caves, counter
    start_caves = []
    with open('input.txt', 'r') as file:
        while line := file.readline():
            temp = start_caves.append(line[:-1].split("-")[0] if line[:-1].split("-")[0] != "start" else line[:-1].split("-")[1]) if line[:-1].split("-")[0] == "start" or line[:-1].split("-")[1] == "start" else caves.append((line[:-1].split("-")[0], "end")) if line[:-1].split("-")[1] == "end" else caves.append((line[:-1].split("-")[1], "end")) if line[:-1].split("-")[0] == "end" else (line[:-1].split("-")[0], line[:-1].split("-")[1])
            if temp is not None:
                caves.append(temp)
                caves.append(temp[::-1])
    for s in start_caves:
        paths = ["start"]
        find_paths(s, paths)
    print(counter) 

def find_paths(current, paths):
    global counter, caves
    if current == "end":
        paths.append("end")
        counter += 1
        return
    if current.islower():
        if paths.count(current) < 1:
            for t in paths:
                if t[0] == current and t[1].islower() and paths.count(t[1]) > 1:
                    return 
            paths.append(current)
        else:
            return
    else:
        paths.append(current)
    for c in caves:
        if c[0] == current:
            temp = [x for x in paths]
            find_paths(c[1], temp)
    return 

main()
