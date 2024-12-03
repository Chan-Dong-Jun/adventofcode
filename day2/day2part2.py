def test(line):
    valid = True
    line = [int(num) for num in line.split()]
    damper = True
    direction = "increasing" if line[1] > line[0] else "decreasing"
    for i in range(len(line)-1):
        if "increasing" and not 1 <= line[i+1] - line[i] <= 3:
            if damper:
                damper = False
            else:
                valid = False
                print(line[1])
                print("trigger1")
                break
        if "decreasing" and not 1 <= line[i] - line[i+1] <= 3:
            if damper:
                damper = False
            else:
                valid = False
                print("trigger2")
                break
    print(line)
    print(damper)
    print(valid)
    return 1 if valid else 0
        
res = 0

with open('day2.txt', 'r') as fh:
    for line in fh:
        res += test(line)
print(res)
