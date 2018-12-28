def main():
	try:
		x=int(input())
		z=int(input())
		x=x^z
		z=x^z
		x=x^z
		print(x,z);
	except:
		print('invalid');
main()
