import re

res = 0

with open('day3.txt', 'r') as fh:
    mul_list = []
    for line in fh:
        mul_list.extend(re.findall(r"mul\(\d+,\d+\)", line))
print(mul_list)
for expression in mul_list:
    first_num, second_num = re.findall(r"\d+", expression)
    res += int(first_num) * int(second_num)
print(res)
                
