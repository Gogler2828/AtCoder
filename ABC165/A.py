K = int(input())
A,B = map(int,input().split())
mes = 0
for num in range (A,B+1):
    if num % K == 0 : mes = 1
    else : pass

if mes == 1 : print("OK")
else : print("NG")