def main():
	try:
		a=0
		x=int(input())
		while(x!=0):
			x=x/2
			if x==1:
				a=1
				break
		if a!=1:
			print('no');
		else :
			print('yes');
	except:
		print('invalid');
main()
