def hasvowel():
	v=['a','e','i','o','u','A','E','I','O','U']
	s=input()
	for x in s:
		if x in v:
			return 'yes'
	return 'no'
try:
    hasvowel()
except:
    print('invalid');
