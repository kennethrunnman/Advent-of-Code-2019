import math
def read_file():
    f = open("input.txt","r")
    contents = f.readlines()
    return contents

def get_array_size(contents):
    max_right = 0
    max_left = 0
    max_up = 0
    max_down = 0
    current_index = [0, 0]
    first_wire = contents[0].split(",")
    second_wire = contents[1].split(",")
    input = first_wire + second_wire
    for d in input:
        if d.startswith("R"):
            number = int(d.strip().split("R")[1])
            current_index[0] += number
            if(current_index[0] > max_right):
                max_right = current_index[0]
        elif d.startswith("L"):
            number = int(d.strip().split("L")[1])
            current_index[0] -= number
            if(current_index[0] < max_left):
                max_left = current_index[0]
        elif d.startswith("U"):
            number = int(d.strip().split("U")[1])
            current_index[1] -= number
            if(current_index[1] < max_up):
                max_up = current_index[1]
        elif d.startswith("D"):
            number = int(d.strip().split("D")[1])
            current_index[1] += number
            if(current_index[1] > max_down):
                max_down = current_index[1]
        else:
            print("Something is Wrong")
    array = [["." for i in range(max_right+abs(max_left)+1)] for j in range(abs(max_up)+max_down+1)]
    origo = [abs(max_up), abs(max_left)]
    return array, origo

def path(origo, array, contents):
    startx = origo[0]
    starty = origo[1]
    current_index = [startx, starty]
    print("start", current_index)
    array[origo[0]][origo[1]] = "O"
    intersections = []
    print("origo", origo)
    old_origo = origo
    first_wire = contents[0].split(",")
    second_wire = contents[1].split(",")
    for d in first_wire:
        if d.startswith("R"):
            number = int(d.strip().split("R")[1])
            for i in range(current_index[1], current_index[1]+number+1):
                if(array[current_index[0]][i] == "|"):
                    array[current_index[0]][i] = "+"
                elif(array[current_index[0]][i] == "O"):
                    continue
                else:
                    array[current_index[0]][i] = "-"
            current_index[1] += number
        elif d.startswith("L"):
            number = int(d.strip().split("L")[1])
            for i in range(current_index[1], current_index[1]-number-1,-1):
                if(array[current_index[0]][i] == "|"):
                    array[current_index[0]][i] = "+"
                elif(array[current_index[0]][i] == "O"):
                    continue
                else:
                    array[current_index[0]][i] = "-"
            current_index[1] -= number
        elif d.startswith("U"):
            number = int(d.strip().split("U")[1])
            for i in range(current_index[0], current_index[0]-number-1, -1):
                if(array[i][current_index[1]] == "-"):
                    array[i][current_index[1]] = "+"
                elif(array[i][current_index[1]] == "O"):
                    continue
                else:
                    array[i][current_index[1]] = "|"
            current_index[0] -= number
        elif d.startswith("D"):
            number = int(d.strip().split("D")[1])
            for i in range(current_index[0], current_index[0]+number+1):
                if(array[i][current_index[1]] == "-"):
                    array[i][current_index[1]] = "+"
                elif(array[i][current_index[1]] == "O"):
                    continue
                else:
                    array[i][current_index[1]] = "|"
            current_index[0] += number
        else:
            print("Something is Wrong")

    # for i in array:
    #     print(i)
    startx = origo[0]
    starty = origo[1]
    current_index = [startx, starty]
    for d in second_wire:
        if d.startswith("R"):
            number = int(d.strip().split("R")[1])
            for i in range(current_index[1], current_index[1]+number+1):
                if(array[current_index[0]][i] == "||"):
                    array[current_index[0]][i] = "*"
                elif(array[current_index[0]][i] == "O"):
                    continue
                elif(array[current_index[0]][i] == "|"):
                    array[current_index[0]][i] = "X"
                    intersections.append([current_index[0], i])
                else:
                    array[current_index[0]][i] = "="
            current_index[1] += number
        elif d.startswith("L"):
            number = int(d.strip().split("L")[1])
            for i in range(current_index[1], current_index[1]-number-1,-1):
                if(array[current_index[0]][i] == "||"):
                    array[current_index[0]][i] = "*"
                elif(array[current_index[0]][i] == "O"):
                    continue
                elif(array[current_index[0]][i] == "|"):
                    array[current_index[0]][i] = "X"
                    intersections.append([current_index[0], i])
                else:
                    array[current_index[0]][i] = "="
            current_index[1] -= number
        elif d.startswith("U"):
            number = int(d.strip().split("U")[1])
            for i in range(current_index[0], current_index[0]-number-1, -1):
                if(array[i][current_index[1]] == "="):
                    array[i][current_index[1]] = "*"
                elif(array[i][current_index[1]] == "O"):
                    continue
                elif(array[i][current_index[1]] == "-"):
                    array[i][current_index[1]] = "X"
                    intersections.append([i, current_index[1]])
                else:
                    array[i][current_index[1]] = "||"
            current_index[0] -= number
        elif d.startswith("D"):
            number = int(d.strip().split("D")[1])
            for i in range(current_index[0], current_index[0]+number+1):
                if(array[i][current_index[1]] == "="):
                    array[i][current_index[1]] = "*"
                elif(array[i][current_index[1]] == "O"):
                    continue
                elif(array[i][current_index[1]] == "-"):
                    array[i][current_index[1]] = "X"
                    intersections.append([i, current_index[1]])
                else:
                    array[i][current_index[1]] = "||"
            current_index[0] += number
        else:
            print("Something is Wrong")

    # for i in array:
    #     print(i)

    #print(intersections)
    nearest = 9999999
    nearest_index = [-1, -1]
    for x in intersections:
        #distance = math.sqrt(math.pow(origo[0]-x[0], 2)+math.pow(origo[1]-x[1], 2))
        #print(distance)
        distance = abs(origo[0]-x[0])+abs(origo[1]-x[1])
        #print(distance, x, origo)
        if distance < nearest:
            nearest = distance
            nearest_index = x
    print("best", nearest, nearest_index)
    #taxi_distance = abs(origo[0]-nearest_index[0])+abs(origo[1]-nearest_index[1])
    #print(taxi_distance)

    best_time = 9999999999
    for intersection in intersections:
        startx = origo[0]
        starty = origo[1]
        current_index = [startx, starty]
        counter = 0
        counting = True
        for d in first_wire:
            if d.startswith("R"):
                number = int(d.strip().split("R")[1])
                for i in range(current_index[1]+1, current_index[1]+number+1):
                    if(counting):
                        counter += 1
                        #print("Counter", current_index[0], i)
                    else:
                        continue
                    if(current_index[0] == intersection[0] and i == intersection[1]):
                        counting = False
                current_index[1] += number
            elif d.startswith("L"):
                number = int(d.strip().split("L")[1])
                for i in range(current_index[1]-1, current_index[1]-number-1, -1):
                    if(counting):
                        counter += 1
                        #print("Counter", current_index[0], i)
                    else:
                        continue
                    if(current_index[0] == intersection[0] and i == intersection[1]):
                        counting = False
                current_index[1] -= number
            elif d.startswith("U"):
                number = int(d.strip().split("U")[1])
                for i in range(current_index[0]-1, current_index[0]-number-1, -1):
                    if(counting):
                        counter += 1
                        #print("Counter", i, current_index[1])
                    else:
                        continue
                    if(i == intersection[0] and current_index[1] == intersection[1]):
                        counting = False
                current_index[0] -= number
            elif d.startswith("D"):
                number = int(d.strip().split("D")[1])
                for i in range(current_index[0]+1, current_index[0]+number+1):
                    if(counting):
                        counter += 1
                        #print("Counter", i, current_index[1])
                    else:
                        continue
                    if(i == intersection[0] and current_index[1] == intersection[1]):
                        counting = False
                current_index[0] += number
            else:
                print("Something is Wrong")
        #print(counter, "first")

        startx = origo[0]
        starty = origo[1]
        current_index = [startx, starty]
        counting = True
        for d in second_wire:
            if d.startswith("R"):
                number = int(d.strip().split("R")[1])
                for i in range(current_index[1]+1, current_index[1]+number+1):
                    if(counting):
                        counter += 1
                        #print("Counter", current_index[0], i)
                    else:
                        continue
                    if(current_index[0] == intersection[0] and i == intersection[1]):
                        counting = False
                current_index[1] += number
            elif d.startswith("L"):
                number = int(d.strip().split("L")[1])
                for i in range(current_index[1]-1, current_index[1]-number-1,-1):
                    if(counting):
                        counter += 1
                        #print("Counter", current_index[0], i)
                    else:
                        continue
                    if(current_index[0] == intersection[0] and i == intersection[1]):
                        counting = False
                current_index[1] -= number
            elif d.startswith("U"):
                number = int(d.strip().split("U")[1])
                for i in range(current_index[0]-1, current_index[0]-number-1, -1):
                    if(counting):
                        counter += 1
                        #print("Counter", i, current_index[1])
                    else:
                        continue
                    if(i == intersection[0] and current_index[1] == intersection[1]):
                        couting = False
                current_index[0] -= number
            elif d.startswith("D"):
                number = int(d.strip().split("D")[1])
                for i in range(current_index[0]+1, current_index[0]+number+1):
                    if(counting):
                        counter += 1
                        #print("Counter", i, current_index[1])
                    else:
                        continue
                    if(i == intersection[0] and current_index[1] == intersection[1]):
                        counting = False
                current_index[0] += number
            else:
                print("Something is Wrong")
        if(best_time > counter):
            best_time = counter
        #print(counter, intersection)
    print(best_time)



def main():
    contents = read_file()
    array, origo = get_array_size(contents)
    path(origo, array, contents)
    return

main()
