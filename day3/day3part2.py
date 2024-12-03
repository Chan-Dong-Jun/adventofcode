import re

res = 0

with open('day3.txt', 'r') as fh:
    mul_list = []
    for line in fh:
        mul_list.extend(re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line))
print(mul_list)
do = True
for expression in mul_list:
    if expression == "do()":
        do = True
    elif expression == "don't()":
        do = False
    elif do:
        first_num, second_num = re.findall(r"\d+", expression)
        res += int(first_num) * int(second_num)
print(res)
