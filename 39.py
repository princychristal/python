def maxl(l):
	max=0
	for x in l:
		if max<x:
			max=x
	print(max);
def main():
	try:
		l=[1,2,3,5,4,77,4,24,52,4]
		maxl(l)
	except:
		print('invalid');
main()
