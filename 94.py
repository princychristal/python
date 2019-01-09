def kthno():
	a=[]
	(b,c)=map(int,sys.stdin.readline().split())
	for x in range(b):
		a.append(int(input()))
	print(a[c-1]);
try:
	kthno()
except:
	print('invalid');
