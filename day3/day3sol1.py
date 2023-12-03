import re
f = open('day3input.txt', 'r')

data = f.readlines()

grid = {}

for lineindex,each in enumerate(data):
    grid[lineindex] = {}
    for charindex, char in enumerate(each):
        grid[lineindex][charindex] = char

for each in grid:
    del grid[each][140]

numbers = {}
guid = 0

for each in grid:
    char = 0
    while char < len(grid[each]):
        try:
            if grid[each][char].isdigit() and grid[each][char+1].isdigit() and grid[each][char+2].isdigit():
                numbers[guid] = {'x': each, 'y':[char,(char+1),(char+2)],'number':int(grid[each][char]+grid[each][char+1]+grid[each][char+2])}
                guid += 1
                char += 3
        except:
            pass
        try:
            if grid[each][char].isdigit() and grid[each][char+1].isdigit():
                numbers[guid] = {'x': each, 'y':[char,char+1],'number':int(grid[each][char]+grid[each][char+1])}
                guid += 1
                char += 2
        except:
            pass
        try:
            if grid[each][char].isdigit():
                numbers[guid] = {'x': each, 'y':[char],'number':int(grid[each][char])}
                guid += 1
                char += 1
        except:
            pass
        char += 1




for each in numbers:
    xcor = [numbers[each]['x']-1,numbers[each]['x'],numbers[each]['x']+1]
    ycor = numbers[each]['y']

    ycor.append(ycor[-1]+1)
    ycor.insert(0, int(str(ycor[0]))-1)

    numbers[each]['cor'] = {'xcor': xcor,'ycor': ycor}

allowed = ['0','1','2','3','4','5','6','7','8','9','.']

part_numbers = []

print(numbers[0]['number'])

for each in numbers:
    for xcor in numbers[each]['cor']['xcor']:
        for ycor in numbers[each]['cor']['ycor']:
            try:
                if grid[xcor][ycor] not in allowed:
                    part_numbers.append(numbers[each]['number'])
            except:
                pass

print(sum(part_numbers))
