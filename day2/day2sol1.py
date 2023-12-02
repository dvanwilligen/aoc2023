import re

allowed = {
    'red': 12,
    'green': 13,
    'blue': 14
}

f = open('day2input.txt', 'r')

data = f.readlines()

good_ids = {}
for i in range(1,101):
    good_ids[str(i)] = i



for each in data:
    id = each.split(':')[0].split(' ')[1].strip()
    sets = each.split(':')[1].split(';')
    for each in sets:
        units = each.split(',')
        for each in units:
            unit = each.split(',')
            print(unit)
            if 'red' in str(unit):
                if int(re.sub(r'\D', '', str(unit))) > 12:
                    try:
                        del good_ids[str(id)]
                    except:
                        pass
            if 'gree' in str(unit):
                if int(re.sub(r'\D', '', str(unit))) > 13:
                    try:
                        del good_ids[str(id)]
                    except:
                        pass
            if 'blue' in str(unit):
                if int(re.sub(r'\D', '', str(unit))) > 14:
                    try:
                        del good_ids[str(id)]
                    except:
                        pass


final = 0

for each in good_ids:
    final += int(each)

print(final)