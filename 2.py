#2a
def fn(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fn(n-1)+fn(n-2)
num=int(input("enter "))
if num>0:
  print(fn(num))
else:
  print("Invalid")

#2b
def BinToDec(b):
    return int(b,2)
print("Enter the Binary Number: ", end = " ")
bnum = input()
dnum = BinToDec(bnum)
print("The decimal value is: ", dnum)
def OctTOHex(o):
    return hex(int(o,8))
print("Enter the Octal number: ", end = " ")
onum = input()
hnum = OctTOHex(onum)
print("The Hexadecimal value is: ", hnum[2:].upper())
