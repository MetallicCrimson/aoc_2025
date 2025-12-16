import time

lines = []
start_time = time.time()
acc = 0

#with open('test_input_p2.txt') as f:
with open('test_input_p2_2.txt') as f:
#with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

machines = {}
memo_table = {}
unchecked_fields = []
for line in lines:
    (temp_in, temp_out) = line.split(":")
    machines[temp_in] = temp_out.split()
    # array for easy modification, but it's fixed to have length 4
    # TT, TF, FT, FF (dac, fft)
    memo_table[temp_in] = [0,0,0,0]
    unchecked_fields.append(temp_in)

queue = []
for m in machines:
    if len(machines[m]) == 1 and machines[m][0] == "out":
        queue.append(m)
        memo_table[m][3] += 1

def get_connections(field):
    acc = []
    for m in machines:
        if field in machines[m]:
            acc.append(m)

    return acc

def add_to_memo(current_field, current_in):
    for i in range(4):
        memo_table[current_in][i] += memo_table[current_field][i]
    print("a", current_field, memo_table[current_in])


while queue:
    current_field = queue.pop(0)

    outs = machines[current_field]
    flag = False
    for o in outs:
        if o in queue:
            flag = True
            break

    if flag:
        print("Postponed!")
        queue.append(current_field)
        continue
    print(current_field, memo_table[current_field])

    if current_field == "fft":
        memo_table[current_field][2] += memo_table[current_field][3]
        memo_table[current_field][3] = 0
        memo_table[current_field][0] += memo_table[current_field][1]
        memo_table[current_field][1] = 0
    elif current_field == "dac":
        memo_table[current_field][1] += memo_table[current_field][3]
        memo_table[current_field][3] = 0
        memo_table[current_field][0] += memo_table[current_field][2]
        memo_table[current_field][2] = 0

    ins = get_connections(current_field)
    for current_in in ins:
        #print(current_field, current_in)
        add_to_memo(current_field, current_in)
        if current_in not in queue:
            queue.append(current_in)
        else:
            queue.remove(current_in)
            queue.append(current_in)

    print(current_field, memo_table[current_field])


print(memo_table)

acc = memo_table["svr"][0]

print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")