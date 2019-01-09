def lex():
	a=input()
	b=list(a)
	b.sort()
	c=''.join(b)
	print(c)
try:
	lex()
except:
	print('invalid');
