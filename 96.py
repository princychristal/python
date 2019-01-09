n=int(input("Enter any number"))
a=0
for x in range(1,n+1):
	if(n%x==0):
		a=a+1
if(a>2):
	print("composite");
else:
        print("Not composite");
