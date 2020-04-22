a,b,c,d = input()
listo = [a,b,c,d]
listo.sort()
if (listo[0]==listo[1])and(listo[1]!=listo[2])and(listo[2]==listo[3]) : print("Yes")
else : print("No")