import time

lines = []
start_time = time.time()
acc = 0

with open('full_input.txt') as f:
#with open('test_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

def find_biggest_pos(line, d):
    biggest_digit_pos = d
    for digit_pos in range(d, len(line)):
        if line[digit_pos] > line[biggest_digit_pos]:
            biggest_digit_pos = digit_pos

    return biggest_digit_pos

for line in lines:
    first_pos = find_biggest_pos(line, 0)
    if first_pos == len(line)-1:
        second_pos = find_biggest_pos(line[:-1], 0)
    else:
        second_pos = find_biggest_pos(line, first_pos+1)

    if first_pos > second_pos:
        (first_pos, second_pos) = (second_pos, first_pos)
    
    # print(line[first_pos], line[second_pos])
    acc += int(line[first_pos] + line[second_pos])


print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")