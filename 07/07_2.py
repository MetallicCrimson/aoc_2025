import time

lines = []
start_time = time.time()

#with open('completed_test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('completed_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

width = len(lines[0])
height = len(lines)

beams = []
splitters = {}

for x in range(width):
    if lines[height-1][x] == "|":
        beams.append((x, height-1, 1))


final_acc = 0

def travel_beam(beam):
    (x, y, acc) = beam
    beams.pop(0)
    # print(beam)

    if not acc:
        # print("None")
        acc = splitters[(x,y)]

    if lines[y-1][x] == "S":
        global final_acc
        final_acc = acc
    elif lines[y-1][x] == "|":
        beams.append(((x,y-1, acc)))
        #print("Inserted", beams[0])
    
    if x > 0 and lines[y][x-1] == "^" and lines[y-1][x-1] != ".":

        if (x-1,y-1) not in splitters:
            splitters[(x-1,y-1)] = acc
            beams.append((x-1,y-1, None))
        else:
            splitters[(x-1,y-1)] += acc
            # print(x-1,y)
            beams.remove((x-1,y-1, None))
            beams.append((x-1,y-1, None))
            # print("Added", splitters[(x-1, y)], acc)

    if x < width-1 and lines[y][x+1] == "^" and lines[y-1][x+1] != ".":
        if (x+1,y-1) not in splitters:
            splitters[(x+1,y-1)] = acc
            beams.append((x+1,y-1, None))
        else:
            splitters[(x+1,y-1)] += acc
            # print(beams)
            beams.remove((x+1,y-1, None))
            beams.append((x+1,y-1, None))

        
while True:
    if not beams:
        break
    else:
        travel_beam(beams[0])

# print(splitters)



print("The final answer is", final_acc)
print("Code executed in", (time.time() - start_time), "seconds")