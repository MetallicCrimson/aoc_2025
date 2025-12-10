import time

lines = []
start_time = time.time()

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

acc = 0
counter = 0

def handle_presses(lights, press):
    for p1 in press:
        for p2 in p1:
            if lights[p2] == ".":
                lights = lights[:p2] + "#" + lights[p2+1:]
            else:
                lights = lights[:p2] + "." + lights[p2+1:]

    #print(lights)
    return lights



for line in lines:
    # print(counter)
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

    for b in buttons:
        queue.append([b])

    while queue:
        current_press = queue.pop(0)
        if handle_presses("." * len(lights), current_press) == lights:
            fewest_press = current_press
            break
        
        for b in buttons:
            if b not in current_press:
                queue.append(current_press + [b])
            

    acc += len(fewest_press)
    # print(lights)
    # print(joltages)
    # print(buttons)


print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")