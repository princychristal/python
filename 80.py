def odddig():
	a=int(input())
	b=[]
	while(a!=0):
		b.append(a%10)
		a//=10
	for x in range(len(b)-1,-1,-1):
		if b[x]%2!=0:
			print(b[x]);
try:
	odddig()
except:
	print('invalid');
