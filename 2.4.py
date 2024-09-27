import re
s = input()
if len(re.findall(r'^#\w\w\w\w\w\w', s)) == 0:
    print('Не соответствует формату')
else:
    print('Соответствует формату')