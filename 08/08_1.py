import time
import math

lines = []
start_time = time.time()

with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
#with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

boxes = []
for line in lines:
    (x,y,z) = line.split(",")
    boxes.append((x,y,z))

# what even?
all_pairs = []
max_pairs = 10

smallest_for_each = {}

def get_distance(box1, box2):
    (x1,y1,z1) = box1
    (x2,y2,z2) = box2
    (x1,y1,z1) = int(x1), int(y1), int(z1)
    (x2,y2,z2) = int(x2), int(y2), int(z2)

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def insert_into_list(box1, box2):
    print(len(all_pairs))

    current_distance = get_distance(box1, box2)
    flag = False

    for i in range(len(all_pairs)):
        if current_distance < all_pairs[i][2]:
            all_pairs.insert(i, (box1, box2, current_distance))

            if len(all_pairs) > max_pairs:
                all_pairs.pop()
            break

    if not flag and len(all_pairs) < max_pairs: ## have to modify this one!!!
        all_pairs.append((box1, box2, current_distance))

for i in range(len(boxes)):
    (x1,y1,z1) = boxes[i]

    for j in range(i+1, len(boxes)):
        (x2,y2,z2) = boxes[j]
        
        insert_into_list((x1,y1,z1), (x2,y2,z2))


#print(all_pairs)

circuits = []

for a in all_pairs:
    flag = False

    (box1, box2) = a[0], a[1]
    for c in circuits:
        b1_in = box1 in c
        b2_in = box2 in c

        if b1_in and b2_in:
            flag = True
            continue
        elif b1_in:
            flag = True
            c.append(box2)
        elif b2_in:
            flag = True
            c.append(box1)

    if not flag:
        circuits.append([box1, box2])

print(all_pairs)

for c in circuits:
    print(c)


#print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")