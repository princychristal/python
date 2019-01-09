def s1to2():
	a=input()
	b=list(a)
	(c,o)=('','')
	for x in range(len(b)):
		if x%2==0:
			c+=b[x]
		else :
			o+=b[x]
	print(c,o);
try:
	s1to2()
except:
	print('invalid');
