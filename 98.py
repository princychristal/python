def changed():
	a=int(input())
	b=[]
	for i in range(a):
		b.append(int(input()))
	for i in range(1,a):
		if b[i-1]>b[i]:
			print(b[i-1]);
			break
try:
	changed()
except:
	print('invalid');
