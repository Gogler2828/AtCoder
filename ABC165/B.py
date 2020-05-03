import math
X = int(input())
mon = 100
for num in range (1,999999999999999900):
    mon = mon + math.floor(mon*0.01)

    if mon >= X : break

print(num)