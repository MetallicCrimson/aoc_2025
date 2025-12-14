## Part2 is NOT finished.
## But since I've thought it would be funny to document my failure,
## here are the approaches I've tried, without knowing linear algebra.

## This files uses BFS or something.

import time

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
        buttons[-1] = list(map(int, buttons[-1]))
        #buttons[-1] = buttons[-1].split(",")

    joltages = list(map(int, joltages))

    queue = []

    # pass button press counts instead of the individual buttons!
    for i in range(len(buttons)):
        # queue.append(([0] * len(buttons), handle_press([0]*len(joltages), buttons[i]), i))
        queue.append(([0] * len(buttons), handle_press([0]*len(joltages), buttons[i]), i))
        queue[-1][0][i] = 1
        #print(queue[-1])

    while queue:

        (current_press, current_joltages, prev_i) = queue.pop(0)
        #print(current_press, current_joltages, prev_i)

        # new_joltages = handle_press(current_joltages, buttons[prev_i])
        print(sum(current_press))

        if arr_eq(current_joltages, joltages):
            fewest_press = current_press
            break

        for j in range(prev_i, len(buttons)):
            new_joltages = handle_press(current_joltages.copy(), buttons[j])


            if not_over(new_joltages, joltages):
                queue.append((current_press.copy(), new_joltages.copy(), j))
                queue[-1][0][j] += 1

        #print(queue)

        # (current_press, current_joltages, prev_i) = queue.pop(0)
        # print(current_press)
        # new_joltages = handle_press(current_joltages, buttons[prev_i])


        # if arr_eq(new_joltages, joltages):
        #     fewest_press = current_press
        #     break
        # for j in range(prev_i, len(buttons)):

        #     queue.append((current_press.copy(), handle_press(current_joltages, buttons[j]), j))
        #     #print(queue)
        #     queue[-1][0][j] += 1

            
    print(fewest_press)
    for f in fewest_press:
        acc += f
    # print(lights)
    # print(joltages)
    # print(buttons)

# print(handle_press([0, 0, 0, 0], [3]))

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")