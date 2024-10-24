n=int(input())
u=0
p=0
c=0
h = list(map(int, input().split()))
for i in range(n):
    if(h[i]>0):
        p+=h[i]
    elif(h[i]==-1  and p!=0):
        p-=1
    else:
        u+=1    
print(u)