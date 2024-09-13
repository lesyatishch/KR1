n = int(input())
i = 1
squared = 1
squares = []
while squared < n:
    squares.append(squared)
    i +=1
    squared = i**2
print(*squares, sep=", ", end='\n')