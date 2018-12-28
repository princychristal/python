
def avg(a,b):
	sum=0
	for x in range(b):
		sum+=a[x]
	print(sum/b);
def main():
	try:
		b=int(input())
		a=[]
		for x in range(b):
			a.append(int(input()))
		avg(a,b)
	except:
		print('invalid');
main()
