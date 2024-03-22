#1a
m1=int(input("Enter the marks for test1 "))
m2=int(input("Enter the marks for test2 "))
m3=int(input("Enter the marks for test3 "))
if m1<=m2 and m1<=m3:
  avg=(m2+m3)/2
if m2<=m1 and m2<=m3:
  avg=(m1+m3)/2
if m3<=m1 and m3<=m2:
  avg=(m1+m2)/2
print("Average marks is",avg)

#1b
val=input()
if val==val[::-1]:
  print("Palindrome")
else:
  print("Not a plaindrome")
for i in range(10):
  if val.count(str(i))>0:
    print(str(i)," appears ",val.count(str(i))," times")
