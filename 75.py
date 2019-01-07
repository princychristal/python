 def midchenge():
	a=input()
	b=len(a)
	c=list(a)
	a=''
	if b%2!=0:
		for x in range(b//2):
			a+=c[i]
		a+='*'
		y=b//2+1
	else:
		for x in range(b//2-1):
			a+=c[x]
		a+='**'
		y=b//2+1
	for x in range(y,b):
		a+=c[x]
	print(a);
try:
	midchenge()
except:
	print('invalid');
