a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = 0
value = a
print("Arithmetic Progression Series : ", end = " ")
for i in range(n):
    print("%d + " %value, end = " ")
    total = total + value
    value = value + d

print("\nThe Sum of Arithmetic Progression Series is %d = %d " %(n, total))
