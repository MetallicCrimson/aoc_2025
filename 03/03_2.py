import time

lines = []
start_time = time.time()
acc = 0

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

line_length = len(lines[0])

def find_biggest_pos(line, d1, d2):
    # print("d1, d2:", d1, d2)
    biggest_digit_pos = d1
    for digit_pos in range(d1, d2):
        if line[digit_pos] > line[biggest_digit_pos]:
            biggest_digit_pos = digit_pos

    return biggest_digit_pos

for line in lines:

    temp_acc = []

    for i in range(12):
        current_pos = temp_acc[-1] if temp_acc else -1
        
        current_biggest = find_biggest_pos(line, current_pos+1, line_length-12+i+1)
        temp_acc.append(current_biggest)

    temp = ""
    for t in temp_acc:
        temp += line[t]
    
    acc += int(temp)


print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")