def factors():
	a=int(input())
	b=[]
	c=0
	for x in range(1,a//2+1):
		if a%x==0:
			b.append(x)
	b.append(a)
	for x in b:
		print(x);
try:
	factors()
except:
	print('invalid');
