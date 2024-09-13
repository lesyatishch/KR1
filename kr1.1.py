sum = 0
true = 1
while true == 1:
    num = int(input())
    sum = sum + num
    if num == 0:
        num = int(input())
        sum = sum + num
        if num == 0:
            break;
print('Сумма:', sum)