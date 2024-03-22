#3a
sentence=input("Enter a sentence")
words=sentence.split(" ")
print(f"This sentence contains {len(words)} words ")
l=u=n=0
for ch in sentence:
  if '0'<=ch<='9':
    n+=1
  if ch.islower():
    u+=1
  if ch.isupper():
    l+=1
print(f"Upper case {u}")
print(f"lower case {l}")
print(f"number {n}")

#3b
str1=input("Enter ")
str2=input("Enter ")
if len(str1)>len(str2):
  big=len(str1)
  short=len(str2)
else:
  big=len(str2)
  short=len(str1)
matchc=0
for i in range(short):
  if str1[i]==str2[i]:
    matchc+=1
print("Similarity percentage is ",matchc/big)  
