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
beams = []

for i in range(width):
    if lines[0][i] == "S":
        beams.append((i,1))
        break

print(beams)

def line_insert(x, y, s):
    lines[y] = lines[y][:x] + "|" + lines[y][x+1:]

while beams:
    (temp_x, temp_y) = beams[0]
    if temp_x < 0 or temp_x >= width or temp_y >= height:
        beams.pop(0)
    elif lines[temp_y][temp_x] == ".":
        lines[temp_y]
        line_insert(temp_x, temp_y, "|")
        beams.append((temp_x, temp_y+1))
        beams.pop(0)
    elif lines[temp_y][temp_x] == "|":
        beams.pop(0)
    # at this point, the only possibility is a splitter
    else:
        beams.append((temp_x-1, temp_y))
        beams.append((temp_x+1, temp_y))
        beams.pop(0)

# for l in lines:
#     print(l)

acc = 0
for y in range(height):
    for x in range(width):
        if lines[y][x] == "^" and lines[y-1][x] == "|":
            acc += 1

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")