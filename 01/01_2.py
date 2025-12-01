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
    temp_rotated = 0
    rotation = int(line[1:])
    if line[0] == 'R':
        dial += rotation
        temp_rotated = dial // 100
    else:
        if dial == 0:
            temp_rotated += 1

        dial -= rotation
        temp_rotated += dial // 100

        
    dial = dial % 100
    if dial == 0 and line[0] == 'L':
        temp_rotated -= 1
    print("Rotated", line[0], temp_rotated, " times. Dial is", dial)
    acc += abs(temp_rotated)

    # print(dial)
    # if dial == 0:
    #     acc += 1

print("The final password is", acc)
print("Code executed in", (time.time() - start_time), "seconds")