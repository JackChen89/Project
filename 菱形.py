n=int(input())
max=2*n-1
for y in range(0,max,2):
 y+=1
 print((max-y)//2*" "+y*"*")
for x in range(max+1,0,-2):
 x-=1
 print((max-x)//2*" "+x*"*")
