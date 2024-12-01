list_1, list_2 = [], []

# read and parse data
with open('day1.txt', 'r') as fh:
    for line in fh:
        if line:
            num1, num2 = line.split()
            list_1.append(int(num1))
            list_2.append(int(num2))

list_3 = [0 for i in range(max(max(list_1), max(list_2)) + 1)]
list_4 = [0 for i in range(max(max(list_1), max(list_2)) + 1)]

for i in range(len(list_1)):
    list_3[list_1[i]] += 1
    list_4[list_2[i]] += 1

res = 0
for i in range(len(list_1)):
    res += list_1[i] * list_4[list_1[i]]

print(res)
