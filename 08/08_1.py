import time
import math

lines = []
start_time = time.time()

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

boxes = []
for line in lines:
    (x,y,z) = line.split(",")
    boxes.append((int(x),int(y),int(z)))

# what even?
all_pairs = []
max_pairs = 1000

smallest_for_each = {}

def get_distance(box1, box2):
    (x1,y1,z1) = box1
    (x2,y2,z2) = box2
    (x1,y1,z1) = int(x1), int(y1), int(z1)
    (x2,y2,z2) = int(x2), int(y2), int(z2)

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

for i in range(len(boxes)):
    (x1,y1,z1) = boxes[i]

    for j in range(i+1, len(boxes)):
        (x2,y2,z2) = boxes[j]
        
        # insert_into_list((x1,y1,z1), (x2,y2,z2))
        all_pairs.append(((x1, y1, z1), (x2, y2, z2),\
                          get_distance((x1,y1,z1), (x2,y2,z2))))



#print(len(all_pairs))
all_pairs.sort(key=lambda x: x[2])

all_pairs = all_pairs[:max_pairs]
#print(all_pairs)

circuits = []
connections = {}


def find_in_circuits(box):
    for i in range(len(circuits)):
        if box in circuits[i]:
            return i
        
    return -1 #shouldn't even be possible

for pair in all_pairs:
    (box1, box2) = pair[0], pair[1]

    flag1 = False
    flag2 = False

    for c in circuits:
        if box1 in c:
            flag1 = True
        if box2 in c:
            flag2 = True

    if not flag1 and not flag2:
        circuits.append([box1, box2])
    elif flag1 and not flag2:
        temp_i = find_in_circuits(box1)
        circuits[temp_i].append(box2)
    elif flag2 and not flag1:
        temp_i = find_in_circuits(box2)
        circuits[temp_i].append(box1)
    else:
        temp_i1 = find_in_circuits(box1)
        temp_i2 = find_in_circuits(box2)
        if temp_i1 != temp_i2:
            circuits[temp_i1] += circuits[temp_i2]
            circuits.pop(temp_i2)

circuits.sort(key=len, reverse=True)

# for c in circuits:
#     print(c)

# print(len(circuits[0]), len(circuits[1]), len(circuits[2]))

acc = len(circuits[0]) * len(circuits[1]) * len(circuits[2])


print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")