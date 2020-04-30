import math
A,B,C,D = map(int,input().split())
if (math.ceil(A/D)) >= (math.ceil(C/B)) : print("Yes") #小数点切り上げ
else : print("No")