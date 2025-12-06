import time

lines = []
start_time = time.time()

#with open('test_input.txt') as f:
#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

answers = []

def clean_list(l):
    return list(filter(lambda n: n != "", l))


operators = clean_list(lines[-1].split(" "))
width = len(operators)

for o in operators:
    if o == "+":
        answers.append(("+", 0))
    else:
        answers.append(("*", 1))

for i in range(len(lines)-1):
    operands = list(map(lambda n: int(n), clean_list(lines[i].split(" "))))
    for j in range(width):
        if answers[j][0] == "+":
            answers[j] = ("+", answers[j][1] + operands[j])
        else:
            answers[j] = ("*", answers[j][1] * operands[j])

print(answers)

acc = 0
for a in answers:
    acc += a[1]


print("The final answer is", acc)
print("Code executed in", (time.time() - start_time), "seconds")