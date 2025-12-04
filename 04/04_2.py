import time

lines = []
start_time = time.time()

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

def count_paper():
    acc = 0

    for y in range(height):
        for x in range(width):
            if lines[y][x] != ".":
                acc += 1

    return acc

def mark_paper():
    acc = 0

    for y in range(height):
        for x in range(width):
            if lines[y][x] == ".":
                continue

            possible_list = add_all_possible(x, y)
            temp_acc = 0
            for p in possible_list:
                # print(p)
                if lines[p[1]][p[0]] != ".":
                    temp_acc += 1
            # print(temp_acc)
            # lines[y][x] = acc
            lines[y] = lines[y][:x] + str(temp_acc) + lines[y][x+1:]
            # print("New line:",x,y, lines[p[1]])

def remove_paper():
    for y in range(height):
        for x in range(width):
            if lines[y][x].isdigit() and int(lines[y][x]) < 4:
                lines[y] = lines[y][:x] + '.' + lines[y][x+1:]

first_count = count_paper()

acc = 0
# print(count_paper())
while count_paper() != acc:
    acc = count_paper()
    mark_paper()

    remove_paper()
    # print(count_paper())


# print("The final sum is", acc)
# print()
# for line in lines:
#     print(line)

print("The final sum is", first_count-count_paper())
print("Code executed in", (time.time() - start_time), "seconds")