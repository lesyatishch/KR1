num = int(input())
count = 0
while num > 0:
    last_digit = num % 10
    if last_digit == 0: 
        count +=1
    num = num // 10
print('Количество нулей:', count)