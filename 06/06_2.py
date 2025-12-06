import time

lines = []
start_time = time.time()

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        #lines.append(line.strip())
        lines.append(line)
answers = []

def clean_list(l):
    return list(filter(lambda n: n != "", l))


operators = clean_list(lines[-1].split(" "))
width = len(operators)

for o in operators[:-1]:
    if o == "+":
        answers.append(("+", []))
    else:
        answers.append(("*", []))

answers.reverse()
print(answers)

flag = False
answer_counter = 0

for x in range(len(lines[0])-1, -1, -1):
    temp_acc = ""
    for y in range(len(lines)-1):
        if lines[y][x] == "":
            continue
        else:
            temp_acc += lines[y][x]

    if temp_acc.strip() == "":
        if flag:
            answer_counter += 1
            flag = False
    else:
        flag = True
        answers[answer_counter][1].append(int(temp_acc))

# for a in answers:
#     print(a)

acc = 0
for a in answers:
    if a[0] == "+":
        temp_acc = 0
        for aa in a[1]:
            temp_acc += aa
    else:
        temp_acc = 1
        for aa in a[1]:
            temp_acc *= aa

    acc += temp_acc

print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")