def sim():
	(p,n,r)=map(int,sys.stdin.readline().split())
	si=p*n*r/100
	print(math.floor(si));
try:
	sim()
except:
	print('invalid');
