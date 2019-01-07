area():
	a,b=map(float,sys.stdin.readline().split())
	c=a*b
	print(round(c,5));
try:
	area()
except:
	print('invalid');
