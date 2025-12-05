import time

lines = []
start_time = time.time()

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

ranges = []


for line in lines:
    if line == "":
        break
    
    temp = line.split("-")
    ranges.append((int(temp[0]), int(temp[1])))

ranges.sort()
print(ranges)

# reducing ranges v2
for i in range(len(ranges)):
    while True:
        if len(ranges) <= i+1:
            break
        r1 = ranges[i]
        r2 = ranges[i+1]
        if r1[1] >= r2[0]:
            ranges[i] = (r1[0], max(r1[1], r2[1]))
            ranges.pop(i+1)
        else:
            break
        print(i, ranges)

# ...let's assume it's correct
# print(ranges)

acc = 0
for r in ranges:
    acc += r[1] - r[0] + 1

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")