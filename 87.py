import sys
def gcd():
	(a,b)=map(int,sys.stdin.readline().split())
	while(b!=0):
		c=b
		b=a%b
		a=c
	print(a)
try:
	gcd()
except:
	print('invalid');
