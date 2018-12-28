def maxa(a):
	max=0
	for x in l:
		if max<x:
			max=x
	print(max);
def main():
	try:
		a=[1,2,3,5,4,77,4,24,52,4]
		maxa(a)
	except:
		print('invalid');
main()
