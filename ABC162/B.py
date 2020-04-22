N = int(input())
listo = [0]
for num in range(1,N+1):
    if (num%15 == 0):
        listo.append(0)
    elif (num%3 == 0):
        listo.append(0)
    elif (num%5 == 0):
        listo.append(0)
    else:
        listo.append(num)

print(sum(listo))