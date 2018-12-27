def main():
	n=input()
	a=0
	for x in n:
		if x.isnumeric() :
			a=a+1
	print('No of numerics in a string is :%d'%a)

