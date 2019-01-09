import sys
def cuboid():
	a,b,c=map(int,sys.stdin.readline().split())
	print(a*b*c);
try:
	cuboid()
except:
	print('invalid');
