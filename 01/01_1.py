import time

lines = []
start_time = time.time()
dial = 50
acc = 0

with open('full_input.txt') as f:

    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())


for line in lines:
    rotation = int(line[1:])
    if line[0] == 'R':
        dial += rotation
    else:
        dial -= rotation

    dial = dial % 100

    # print(dial)
    if dial == 0:
        acc += 1

print("The final password is", acc)
print("Code executed in", (time.time() - start_time), "seconds")