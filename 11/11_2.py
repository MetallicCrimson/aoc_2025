## Part 2 is unfinished.
## As I already left off day10 part2, I wasn't gonna 100% this year
## - at least not yet. Thus, while I could probably solve this,
## I don't want to spend too much time on it.
## It was a cool attempt though.

import time

lines = []
start_time = time.time()
acc = 0

with open('test_input_p2.txt') as f:
#with open('test_input_p2_2.txt') as f:
#with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

machines = {}
memo_table = {}
for line in lines:
    (temp_in, temp_out) = line.split(":")
    machines[temp_in] = temp_out.split()
    # TT, TF, FT, FF?
    memo_table[temp_in] = [0, 0, 0, 0]

queue = []


for temp_in in machines:
    temp_out = machines[temp_in]
    if len(temp_out) == 1 and temp_out[0] == "out":
        queue.append(temp_in)
        # memo_table[temp_in] = (1, False, False)

# print(queue)

# while queue:
#     current = queue.pop(0)
#     possible_steps = []
#     for input in machines:
#         if current in machines[input]:
#             possible_steps.append(input)

    # for p in possible_steps:
    #     if not memo_table[p]:
    #         memo_table[p] = memo_table[current]
    #         queue.append(p)
    #     else:
    #         memo_table[p] += memo_table[current]
    #         if current == "dac":



def take_step(current_in, dac_done, fft_done):
    #print(current_in)
    current_out = machines[current_in]

    new_dac_done = True if current_in == "dac" else dac_done
    new_fft_done = True if current_in == "fft" else fft_done

    # if new_dac_done and new_fft_done:
    #     memo_table[current_in][0] += 1
    # elif new_dac_done and not new_fft_done:
    #     memo_table[current_in][1] += 1
    # elif new_dac_done and not new_fft_done:
    #     memo_table[current_in][2] += 1
    # elif new_dac_done and not new_fft_done:
    #     memo_table[current_in][3] += 1
    # else:
    #     print("What the fuck")

    if not dac_done and new_dac_done:
        if not new_fft_done:
            memo_table[current_in][1] = memo_table[current_in][3]
            memo_table[current_in][3] = 0
        else:
            memo_table[current_in][0] = memo_table[current_in][2]
            memo_table[current_in][2] = 0
    elif not fft_done and new_fft_done:
        if not new_dac_done:
            memo_table[current_in][2] = memo_table[current_in][3]
            memo_table[current_in][3] = 0
        else:
            memo_table[current_in][0] = memo_table[current_in][1]
            memo_table[current_in][1] = 0


    if len(current_out) == 1 and current_out[0] == "out":
        # print("Heyo")
        return memo_table[current_in][3]
    else:
        acc = 0
        for c in current_out:
            if new_dac_done and new_fft_done:
                memo_table[c][0] += memo_table[current_in][0]
                if memo_table[c][0] == memo_table[current_in][0]:
                    take_step(c, new_dac_done, new_fft_done)
            elif new_dac_done and not new_fft_done:
                memo_table[c][1] += memo_table[current_in][1]
                if memo_table[c][1] == memo_table[current_in][1]:
                    take_step(c, new_dac_done, new_fft_done)
            elif not new_dac_done and new_fft_done:
                memo_table[c][2] += memo_table[current_in][2]
                if memo_table[c][2] == memo_table[current_in][2]:
                    take_step(c, new_dac_done, new_fft_done)
            elif not new_dac_done and not new_fft_done:
                memo_table[c][3] += memo_table[current_in][3]
                if memo_table[c][3] == memo_table[current_in][3]:
                    take_step(c, new_dac_done, new_fft_done)
            else:
                print("What the fuck")

        
        return acc

memo_table["svr"][3] += 1
acc = take_step("svr", False, False)
print(memo_table)
acc = 0

for q in queue:
    acc += memo_table[q][1]


print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")