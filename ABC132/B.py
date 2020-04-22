n = int(input())
p = list(map(int,input().split()))
seconds = []
for a in range(0,n-2):
    num = [p[a],p[a+1],p[a+2]]
    if (num[0]<num[1]<num[2])or(num[2]<num[1]<num[0]):
        seconds.append(p[a+1])
    else : pass

print(len(set(seconds)))