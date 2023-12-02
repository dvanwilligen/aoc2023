import re

f = open('day2input.txt', 'r')

data = f.readlines()

interim = {}

for i in range(1,101):
    interim[str(i)] = {'red':0, 'green':0, 'blue':0}

for each in data:
    id = each.split(':')[0].split(' ')[1].strip()
    sets = each.split(':')[1].split(';')
    for each in sets:
        units = each.split(',')
        for each in units:
            unit = each.split(',')

            if 'red' in str(unit):
                if int(re.sub(r'\D', '', str(unit))) > interim[str(id)]['red']:
                    interim[str(id)]['red'] = int(re.sub(r'\D', '', str(unit)))

            if 'green' in str(unit):
                if int(re.sub(r'\D', '', str(unit))) > interim[str(id)]['green']:
                    interim[str(id)]['green'] = int(re.sub(r'\D', '', str(unit)))

            if 'blue' in str(unit):
                if int(re.sub(r'\D', '', str(unit))) > interim[str(id)]['blue']:
                    interim[str(id)]['blue'] = int(re.sub(r'\D', '', str(unit)))

final = []


for each in interim.values():
    power = each['red'] * each['green'] * each['blue']
    final.append(power)

print(sum(final))