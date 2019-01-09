def sumal():
	a=int(input())
	b=[]
	sum=0
	for x in range(a):
		b.append(int(input()))
		sum+=b[x]
	print(sum);
try:
	sumal()
except:
	print('invalid');
