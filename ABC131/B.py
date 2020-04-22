N,L = map(int,input().split())
deri = [L]
for num in range(1,N):
    deri.append(L+num)

deri.sort()
if (0 in deri) == True:
    deri.remove(0)
elif sum(deri) < 0:
    del deri[-1]
else:
    del deri[0] #del

print(sum(deri))