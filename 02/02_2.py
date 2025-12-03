import time
import math

lines = []
start_time = time.time()
acc = 0

# screw this, i'm hardcoding the permutations
perms = {2: [2], 3: [3], 4: [2,4], 5: [5], 6: [2,3,6], 7: [7], 8: [2,4,8],
         9: [3,9], 10: [2,5,10]}
# print(perms)

with open('full_input.txt') as f:
#with open('test_input.txt') as f:
    temp_lines = f.readlines()

    for line in temp_lines:
        lines.append(line.strip())

id_list = lines[0].split(",")

def check_if_invalid(i, p, digits):

    perm_length = digits // p
    # print("Perm length:", perm_length)
    d1 = i // (10**(digits-perm_length))
    for j in range(1,p):
        d2 = i % (10 ** (digits - j*perm_length))
        d2 //= 10 ** (digits - j*perm_length - perm_length)
        if d2 != d1:
            return False
        
    return True

for id in id_list:
    (first_id, last_id) = id.split("-")
    (first_id, last_id) = (int(first_id), int(last_id))
    for i in range(first_id, last_id+1):
        digits = math.floor(math.log10(i)) + 1
        if digits in perms:
            temp_perms = perms[digits]
            for p in temp_perms:
                # print("Perm:", p)
                if check_if_invalid(i, p, digits):
                    acc += i
                    break

        

print("The final sum is", acc)
print("Code executed in", (time.time() - start_time), "seconds")