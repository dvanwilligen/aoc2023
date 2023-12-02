import re
f = open('day1input.txt', 'r')

data = f.readlines()

step1 = []

for each in data:
    onlynumbers = re.sub(r'\D', '', each)
    step1.append(int(str(onlynumbers[0:1])+str(onlynumbers[-1:])))

print(sum(step1))