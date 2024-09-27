import re
s = input()
count = 0
print(re.sub(r'A', 'aa', s))
print('Количество слов, начинающихся на p = ', re.findall(r'\bp', s).count('p'))