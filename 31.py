a = input("Enter a string : ")
count = 0
for x in a:
  if x.isspace() != True:
    count = count + 1
print("Total number of characters : ",count)
