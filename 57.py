def main():
	try:
		a=int(input())
		b=int(input())
		x=a
		a=b
		b=x
		print(a,b);
	except:
		print('invalid')
main()
