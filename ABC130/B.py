A,X = map(int,input().split())
L = list(map(int,input().split()))
jump = 0
count = 0
while jump >= X:
    jump = jump + L[count]
    count = count + 1
    
print(count)