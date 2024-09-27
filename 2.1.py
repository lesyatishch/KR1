s = input()
integ = 0
dec = -1
dot_found = 0
l = len(s)
for i in range(l):
    if s[i] == '+' or s[i] == '-': 
        continue
    if s[i] == '.':
        dot_found = 1
    if dot_found == 0:
        integ+=1
    else:
        dec+=1
    if i == l-1:
        if dot_found == 0: 
            print('Целое число')
        else:
            print('Число с дробной частью. Количество знаков в целой части = ', integ, 'Кличество знаков в дробной части = ', dec)
    