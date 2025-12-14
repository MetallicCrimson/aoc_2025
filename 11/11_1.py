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

machines = {}
for line in lines:
    (temp_in, temp_out) = line.split(":")
    machines[temp_in] = temp_out.split()

def take_step(current_in):
    print(current_in)
    current_out = machines[current_in]

    if len(current_out) == 1 and current_out[0] == "out":
        return 1
    else:
        acc = 0
        for c in current_out:
            acc += take_step(c)
        
        return acc

acc = take_step("you")


print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")