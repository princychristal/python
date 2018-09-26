l=int(input("l="))
m=int(input("m="))
flag=0
for x in range(l+1,m):
    flag=0
    for y in range(1,x+1):
        if(x%y==0):
            flag=flag+1
    if(flag==2):
         print(x)
