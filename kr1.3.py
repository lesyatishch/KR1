import math
n = int(input())
i = 1
sum = 0
while i <= n:
    fact = 1
    j = 2
    while j <= i:
        fact = fact * j
        j +=1
    sum = sum + 1 / fact
    i +=1
print('Значение выражения:', '{:5.5f}'.format(sum))