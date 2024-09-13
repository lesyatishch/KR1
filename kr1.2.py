n = int(input())
i = 1
sum = 0
while i <= n:
    sum = sum + 1 / i**2
    i +=1
print('Значение выражения:', '{:5.5f}'.format(sum))