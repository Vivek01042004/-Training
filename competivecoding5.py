n=int(input())
g=str(input())
a=0
d=0
for i in range(n):
    if(g[i]=='A'):
        a=a+1
    elif(g[i]=='D'):
        d=d+1
if(a>d):
    print("Anton")
elif(a==d):
    print("Friendship")
else:
    print("Danish")