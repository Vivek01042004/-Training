c=int(input())
if(c>=1 and c<=1000000):
    if(c<5):
        print(1)
    elif(c%5==0):
        print(c//5)
    else:
        print((c//5)+1)  