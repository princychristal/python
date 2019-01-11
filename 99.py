import sys
def sat():
	(x,y,z)=map(int,sys.stdin.readline().split())
	print((x*y)%z);
try:
	sat()
except:
	print('invalid');
