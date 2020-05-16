a,b,c,k = map(int,input().split())

if k <= a :
    print(k) #選ぶ枚数がA枚以下ならば、ポイントはK枚分加算される
elif k <= a + b :
    print(a) #選ぶ枚数がA枚以上A+B枚以下では、ポイントはA枚分だけ加算される
else :
    print(a-(k-(a+b))) #A枚分のポイントからC枚分減らせばポイントとなる