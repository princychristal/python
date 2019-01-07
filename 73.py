def between():
	a=int(input())
	b=int(input())
	c=int(input())
	for i in range(b,c):
		if i==a:
			return 'yes'
	return 'no'
try:
	between()
except:
	print('invalid');
