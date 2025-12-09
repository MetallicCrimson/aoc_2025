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

points = []
all_corners = []

for line in lines:
    (x,y) = line.split(",")
    points.append((int(x), int(y)))

def get_area(p1, p2):
    width = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
    height = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1

    return width * height

for i in range(len(points)):
    (x1,y1) = points[i]

    for j in range(i+1, len(points)):
        (x2,y2) = points[j]
        
        # insert_into_list((x1,y1,z1), (x2,y2,z2))
        all_corners.append(((x1, y1), (x2, y2),\
                          get_area((x1,y1), (x2,y2))))


all_corners.sort(key=lambda x: x[2], reverse=True)

acc = all_corners[0][2]

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")