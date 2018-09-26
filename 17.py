y=int(input("Y="))
t=y
s=0
a=0
while y>0:
    re=y%10
    a=re**3
    s=s+a
    y=y//10

if(t==s):
    print("armstrong")
else:
    print("not armstrong")
