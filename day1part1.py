list_1, list_2 = [], []
res = 0

# read and parse data
with open('day1.txt', 'r') as fh:
    for line in fh:
        if line:
            num1, num2 = line.split()
            list_1.append(num1)
            list_2.append(num2)

list_1.sort()
list_2.sort()

for i in range(len(list_1)):
    res += abs(int(list_1[i]) - int(list_2[i]))

print(res)
