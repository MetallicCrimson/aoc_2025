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
borders = []
max_x = 0
max_y = 0


for line in lines:
    (x,y) = line.split(",")
    points.append((int(x), int(y)))
    if int(x) > max_x:
        max_x = int(x)
    if int(y) > max_y:
        max_y = int(y)

max_x += 1
max_y += 1

def get_path(p1, p2): # should only handle two adjacent points
    if p1[0] == p2[0]:
        temp_range = range(min(p1[1], p2[1]), max(p1[1], p2[1]))
        return ("y", p1[0], temp_range)
    elif p1[1] == p2[1]:
        temp_range = range(min(p1[0], p2[0]), max(p1[0], p2[0]))
        return ("x", p1[1], temp_range)
    else:
        return "Error!"
    
for i in range(len(points)-1):
    borders.append(get_path(points[i], points[i+1]))
borders.append(get_path(points[-1], points[0]))

def get_area(p1, p2):
    width = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
    height = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1

    return width * height

#print(borders)


def check_if_valid(p1, p2):
    for border in borders:
       # print(p1, p2, border)
        if border[0] == "x":
            if border[1] not in range(min(p1[1],p2[1])+1, max(p1[1],p2[1])):
                continue
            
            if border[2].start <= min(p1[0], p2[0]) and border[2].stop > min(p1[0], p2[0]):
                return False
            if border[2].start < max(p1[0],p2[0]) and border[2].stop >= max(p1[0],p2[0]):
                return False

        else:
            #print("Checking y")
            if border[1] not in range(min(p1[0],p2[0])+1, max(p1[0],p2[0])):
                continue

            if border[2].start <= min(p1[1], p2[1]) and border[2].stop > min(p1[1], p2[1]):
                return False
            if border[2].start < max(p1[1],p2[1]) and border[2].stop >= max(p1[1],p2[1]):
                return False

            
    return True
                
for i in range(len(points)):
    (x1,y1) = points[i]

    for j in range(i+1, len(points)):
        (x2,y2) = points[j]
        
        # insert_into_list((x1,y1,z1), (x2,y2,z2))
        if check_if_valid((x1,y1), (x2, y2)):
            all_corners.append(((x1, y1), (x2, y2),\
                            get_area((x1,y1), (x2,y2))))


all_corners.sort(key=lambda x: x[2], reverse=True)

# for a in all_corners:
#     print(a)
acc = all_corners[0][2]


#print(check_if_valid((11,1),(2,5))) 

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")