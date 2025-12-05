import time

lines = []
start_time = time.time()

# with open('test_input.txt') as f:
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

def check_if_valid(i):
    flag = False
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            return True
        
    return False


# print(lines.index("")+1, len(lines))

acc = 0
for i in range(lines.index("")+1, len(lines)):
    # print(lines[i])
    if check_if_valid(int(lines[i])):
        acc += 1

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")