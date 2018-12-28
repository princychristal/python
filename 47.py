def countd(l,b):
	(max,min)=(0,9999)
	for x in range(n):
		if max<l[x]:
			max=l[x]
		if min>l[x]:
			min=l[x]
	print(min,max);
def main():
	try:
		l=[]
		b=int(input())
		for x in range(b):
			l.append(int(input()))
		countd(l,b)
	except:
		print('invalid');
