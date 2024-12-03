res = 0

with open('day2.txt', 'r') as fh:
    for line in fh:
        line = [int(num) for num in line.split()]
        difference = [line[i+1] - line[i] for i in range(len(line)-1)]
        
        print(difference)
        if not ((max(difference) < 0 and min(difference) < 0) or (max(difference) > 0 and min(difference) > 0)):
            continue
        if max(difference) > 3 or min(difference) < -3:
            continue
        res += 1
print(res)
                
