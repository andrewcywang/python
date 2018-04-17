for i in range(10):
    print(i, end=' ')

print()

# 1 .. 10 註解
x = int(input('請問要從一加到幾? '))
sum = 0
for j in range(1, x+1, 1):
    
    if (j==x):
        print(j, end=' = ')
    else:
        print(j, end=' + ')
        
    sum = sum + j

print(sum)

