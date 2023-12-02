f = open('day1input.txt', 'r')

data = f.readlines()

step1 = []

for each in data:
    intermediary1 = []
    string = ""
    string = each
    while len(string) > 0:
        if string.startswith('1'):
            intermediary1.append('1')
        elif string.startswith('2'):
            intermediary1.append('2')
        elif string.startswith('3'):
            intermediary1.append('3')
        elif string.startswith('4'):
            intermediary1.append('4')
        elif string.startswith('5'):
            intermediary1.append('5')
        elif string.startswith('6'):
            intermediary1.append('6')
        elif string.startswith('7'):
            intermediary1.append('7')
        elif string.startswith('8'):
            intermediary1.append('8')
        elif string.startswith('9'):
            intermediary1.append('9')
        elif string.startswith('0'):
            intermediary1.append('0')
        elif string.startswith('one'):
            intermediary1.append('1')
        elif string.startswith('two'):
            intermediary1.append('2')
        elif string.startswith('three'):
            intermediary1.append('3')
        elif string.startswith('four'):
            intermediary1.append('4')
        elif string.startswith('five'):
            intermediary1.append('5')
        elif string.startswith('six'):
            intermediary1.append('6')
        elif string.startswith('seven'):
            intermediary1.append('7')
        elif string.startswith('eight'):
            intermediary1.append('8')
        elif string.startswith('nine'):
            intermediary1.append('9')
        elif string.startswith('zero'):
            intermediary1.append('0')
        else:
            pass
        string = string[1:]

    step1.append(intermediary1)

step2 = []

for each in step1:
    step2.append(int(each[0]+each[-1]))

print(sum(step2))