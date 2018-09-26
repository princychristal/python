y=int(input("NUMBER="))
if(y<=1000):
 t=y
 z=0
 while y>0:
    re=y%10
    z=z*10+re
    y=y//10
 if(t==z):
  print("palindrome")
 else:
    print("not a palindrome")
