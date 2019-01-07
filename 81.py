import sys
 def get():
	a=[]
	a=[]
	while(True):
		try:
			n,m= map(int,sys.stdin.readline().split())
		except ValueError:
			break
		a.append(n)
		a.append(m)
		b.append(a)
		a=[]
	for i in b:
		print(i[1]-i[0]);
try:
	get()
except:
	print('invalid');
