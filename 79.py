import math
def persqr():
	a=int(input())
	b=int(input())
	b*=a
	c=math.sqrt(b)
	if c==int(c):
		print('yes');
	else :
		print('no');
try:
	persqr()
except:
	print('invalid');
