x=(input("N="))
if(x.isalpha()==False):
 n=int(x)
 if(n>0):
  print("positive")
 elif(n<0):
  print("nagative")
 else:
  print("zero")
else:
 print("the input is invalid")
