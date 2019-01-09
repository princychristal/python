def inton():
	a=input()
	b=list(a)
	c=''
	for x in b:
		if x.isnumeric():
			c+=x
	print(c);
try:
	inton()
except:
	print('invalid');
