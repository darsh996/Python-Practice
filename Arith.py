# WAP to find sum mul sq cudbe and avg of two numbers

from audioop import mul
from traceback import print_tb


n1 = int(input("Enter num 1:"))
n2 = int(input("Enter num 2:"))

add = n1 + n2 
mul = n1 * n2
sq1 = n1 * n1
sq2 = n2 * n2
cu1 = sq1* n1
cu2 = sq2* n2
avg = (n1+n2)/2

print("Addition of",n1," and ",n2," is:",add)
print("Multiplication is:",mul)
print("Square of ",n1," is:",sq1)
print("Square of ",n2," is:",sq2)
print("Cube of ",n1," is:",cu1)
print("Cube of ",n2," is:",cu2)
print("Average of ",n1," and ",n2," is:",avg)