def main():
    target_area = []
    with open('input.txt', 'r') as file:
        line = file.readline()[:].split()
        x = list(map(int, line[2][2:-1].split("..")))
        y = list(map(int, line[3][2:].split("..")))
        target_area.append((x[0], y[0]))
        target_area.append((x[1], y[1]))
    
    counter = 0
    for x in range(200):
        for y in range(500, -143, -1):
            start_velocity = (x, y)
            position = (0, 0)
            velocity = start_velocity
            while True:
                position, velocity = step(position, velocity)
                if position[1] < target_area[0][1] or position[0] > target_area[1][0]:
                    break 
                if position[0] >= target_area[0][0] and position[0] <= target_area[1][0]:
                    if position[1] >= target_area[0][1] and position[1] <= target_area[1][1]:
                        counter += 1
                        break
    print(counter) 

def step(position, velocity):
    position = (position[0]+velocity[0], position[1]+velocity[1])
    x = velocity[0]
    y = velocity[1]
    if velocity[0] < 0:
        x += 1
    if velocity[0] > 0:
       x -= 1
    y -= 1
    velocity = (x, y)
    return position, velocity


main()
