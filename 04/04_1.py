import time

lines = []
start_time = time.time()
acc = 0

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

width = len(lines[0])
height = len(lines)

def add_all_possible(x,y):
    acc = []
    if x == 0:
        if y != 0:
            acc += [(x, y-1), (x+1, y-1)]

        acc += [(x+1, y)]

        if y != height-1:
            acc += [(x+1, y+1), (x, y+1)]
    elif x == width-1:
        if y != 0:
            acc += [(x, y-1), (x-1, y-1)]

        acc += [(x-1, y)]

        if y != height-1:
            acc += [(x-1, y+1), (x, y+1)]
    else:
        if y != 0:
            acc += [(x-1, y-1), (x, y-1), (x+1, y-1)]

        acc += [(x-1, y), (x+1, y)]

        if y != height-1:
            acc += [(x-1, y+1), (x+1, y+1), (x, y+1)]

    return acc

for y in range(height):
    for x in range(width):
        if lines[y][x] == ".":
            continue

        possible_list = add_all_possible(x, y)
        temp_acc = 0
        for p in possible_list:
            if lines[p[1]][p[0]] != ".":
                temp_acc += 1

        if temp_acc < 4:
            acc += 1

print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")