## This final file gets the connections between buttons, and
## tries to check all of their possible combinations.
## Incredible optimization compared to the first approach,
## but large input lines still break it.

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

def insert_into_ac(button, method, ac):
    for a in ac:
        for b in a:
            if b[0] == button:
                b = (b[0], method)

def check_ac(ac):
    for a in ac:
        return


def find_in_ac(button, ac):
    return

def find_smallest(range_dir, buttons):
    temp = None
    for k in range_dir:
        r = range_dir[k]

        if temp == None or r[1]-r[0] < temp[1][1]-temp[1][0]:
            # print("Heyo", k)
            if k in buttons:
                temp = (k, r)

    return temp[0]

def find_method(button, assigned, methods):
    # print("B:", button)
    for i in range(len(assigned)):
        a = assigned[i]
        methodless = []
        if button not in a:
            continue
        else:
            methodless = list(filter(lambda x: methods[x] == None, a))
            if len(methodless) == 1:
                a2 = a.copy()
                a2.remove(methodless[0])
                return (i, a2)
            
    return "range"

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

    # print(range_dir)

    # this will be very stupid
    unchecked_buttons = buttons.copy()

    final_queue = []
    button_methods = {}
    for b in buttons:
        button_methods[b] = None


    while unchecked_buttons:
        button_queue = [find_smallest(range_dir, unchecked_buttons)]
        connections = [button_queue[0]]
        while button_queue:
            current_button = button_queue.pop(0)
            if current_button in unchecked_buttons:
                unchecked_buttons.remove(current_button)

            for b in assigned_buttons:
                if current_button in b:
                    unknown = []
                    for b2 in b:
                        if b2 not in connections:
                            unknown.append(b2)
                    
                    if len(unknown) == 1:
                        connections.append(unknown[0])
                        button_queue.append(unknown[0])
            
        # can we assume button_methods doesn't have c...?
        # print("c", connections)
        for c in connections:
            if not final_queue:
                final_queue.append((c, "range"))
                button_methods[c] = "range"
            else:
                if button_methods[c]:
                    temp_method = button_methods[c]
                else:
                    temp_method = find_method(c, assigned_buttons, button_methods)
                    button_methods[c] = temp_method

                final_queue.append((c, temp_method))

    queue = [[None] * len(buttons)]

    print(final_queue)

    break

    for fq in final_queue:
        print(len(queue))
        if fq[1] == "range":
            for i in range(len(queue)):
                print(len(queue))
                q = queue.pop(0)
                for i in range(range_dir[fq[0]][0], range_dir[fq[0]][1]+1):
                    temp_q = q.copy()
                    temp_q[buttons.index(fq[0])] = i
                    queue.append(temp_q)
        else:
            (group, elems) = fq[1]
            # print(elems)
            for q in queue:
                print(len(queue))
                temp = joltages[group]
                for e in elems:
                    print("a")
                    temp -= q[buttons.index(e)]

                q[buttons.index(fq[0])] = temp

    # print(queue)

    # print(button_methods)

    # print(unchecked_buttons)

    # button_queue = [find_smallest(range_dir, unchecked_buttons)]
    # print("another bq", button_queue)
    # connections = [button_queue[0]]

    # while button_queue:
    #     current_button = button_queue.pop(0)
    #     unchecked_buttons.remove(current_button)

    #     for b in assigned_buttons:
    #         if current_button in b:
    #             unknown = []
    #             for b2 in b:
    #                 if b2 not in connections:
    #                     unknown.append(b2)
                
    #             if len(unknown) == 1:
    #                 connections.append(unknown[0])
    #                 button_queue.append(unknown[0])

    # print("c2", connections)
    # print(unchecked_buttons)


    # queue = [[[0] * len(buttons), 0]]
    # for i in range(len(buttons)):
    #     queue[0][0][i] = range_dir[buttons[i]][0]
    # print(queue)

    smallest_press = math.inf
    while queue:
        q = queue.pop(0) 
        if list(filter(lambda x : x < 0, q)):
            continue

        current_joltages = handle_press_new(q, buttons, [0]*len(joltages))
        if arr_eq(current_joltages, joltages):
            if sum(q) < smallest_press:
                smallest_press = sum(q)
        continue
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
    acc += smallest_press


    # print(lights)
    # print(joltages)
    # print(buttons)

# print(handle_press([0, 0, 0, 0], [3]))

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")