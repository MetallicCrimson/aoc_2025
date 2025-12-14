## This file uses ranges, trying to iterate through them all.

import time
import math

lines = []
start_time = time.time()

#with open('test_input.txt') as f:
with open('test_input_2.txt') as f:
#with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

acc = 0
counter = 0

def handle_press(joltages, button):
    #print(joltages, button)
    for b in button:
        joltages[b] += 1

    #print(joltages)
    return joltages

def handle_press_new(presses, buttons, jolt_acc):
    for i in range(len(buttons)):
        button = buttons[i]
        for b in button:
            jolt_acc[b] += presses[i]

    return jolt_acc


def arr_eq(arr1, arr2):
    # assume both arrays have the same length
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
        
    return True

def not_over(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return False
        
    return True

for line in lines:
    print(counter)
    counter += 1
    fewest_press = None
    temp = line.split(" ")
    lights = temp[0][1:-1]
    joltages = temp[-1].split(",")
    joltages[0] = joltages[0][1:]
    joltages[-1] = joltages[-1][:-1]
    temp_buttons = temp[1:-1]
    buttons = []
    for tb in temp_buttons:
        temp2 = tb[1:-1]
        buttons.append(temp2.split(","))
        buttons[-1] = tuple(map(int, buttons[-1]))
        #buttons[-1] = buttons[-1].split(",")

    joltages = list(map(int, joltages))

    assigned_buttons = []
    for i in range(len(joltages)):
        temp_acc = []
        for button in buttons:
            if i in button:
                temp_acc.append(button)

        assigned_buttons.append(temp_acc)

    # print(assigned_buttons)

    range_dir = {}
    for button in buttons:
        range_dir[button] = (0, math.inf)

    for i in range(len(joltages)):
        current_joltage = joltages[i]
        for button in assigned_buttons[i]:
            if range_dir[button][1] > current_joltage:
                range_dir[button] = (range_dir[button][0], current_joltage)

    for i in range(len(joltages)):
        current_joltage = joltages[i]
        if len(assigned_buttons[i]) == 1:
            range_dir[assigned_buttons[i][0]] = (current_joltage, current_joltage)
        elif len(assigned_buttons[i]) == 2:
            if range_dir[assigned_buttons[i][0]][1] < current_joltage:
                range_dir[assigned_buttons[i][1]] = (current_joltage - range_dir[assigned_buttons[i][0]][1], range_dir[assigned_buttons[i][1]][1])
            if range_dir[assigned_buttons[i][1]][1] < current_joltage:
                range_dir[assigned_buttons[i][0]] = (current_joltage - range_dir[assigned_buttons[i][1]][1], range_dir[assigned_buttons[i][0]][1])

    print(range_dir)

    # this will be very stupid

    possible_presses = []

    queue = [[[0] * len(buttons), 0]]
    for i in range(len(buttons)):
        queue[0][0][i] = range_dir[buttons[i]][0]
    print(queue)

    while queue:
        print(len(queue))
        (current_press, prev_i) = queue.pop(0)

        if arr_eq(handle_press_new(current_press, buttons, [0] * len(joltages)), joltages):
            fewest_press = current_press
            break

        for j in range(prev_i, len(buttons)):
            if range_dir[buttons[j]][1] > current_press[j]:
                new_press = current_press.copy()
                new_press[j] += 1


                queue.append((new_press.copy(), j))

        # for j in range(prev_i, len(buttons)):
        #     new_joltages = handle_press(current_joltages.copy(), buttons[j])


        #     if not_over(new_joltages, joltages):
        #         queue.append((current_press.copy(), new_joltages.copy(), j))
        #         queue[-1][0][j] += 1


    # print(fewest_press)
    if fewest_press:
        for f in fewest_press:
            acc += f


    # print(lights)
    # print(joltages)
    # print(buttons)

# print(handle_press([0, 0, 0, 0], [3]))

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")