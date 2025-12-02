import time

lines = []
start_time = time.time()
dial = 50
acc = 0

#with open('test_input_2.txt') as f:
with open('full_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

id_list = lines[0].split(",")

def check_if_invalid(i):
    (first, last) = (str(i)[:len(str(i))//2], str(i)[len(str(i))//2:])
    if len(first) != len(last):
        return False
    
    for j in range(len(first)):
        if first[j] != last[j]:
            return False
        

    return True

for id in id_list:
    (first_id, last_id) = id.split("-")
    (first_id, last_id) = (int(first_id), int(last_id))
    for i in range(first_id, last_id+1):
        if check_if_invalid(i):
            print(i)
            acc += i

print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")