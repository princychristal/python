def countd(i):
	a=0
	while(i!=0):
		i//=10
		a+=1
	print(a);
def main():
	try:
		n=int(input())
		countd(i)
	except:
		print('invalid');
main()
