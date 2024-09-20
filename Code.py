import random
import string
a=input("Enter a string: ")
if len(a)<2:
    a=a[::-1]
    print(a)

elif len(a)>=2:
  add1=input("enter 3 alphabets to the start: ")
  add2=input("enter 3 alphabets to the end: ")
  modified=a[1:]+a[0]
  add=add1+modified+add2
  print(add)
    
# For decoding
b=input("enter the word to decode")
if len(b)<2:
    b=b[::-1]
    print(b)
elif len(b)>=2:
    modified1=b[3:-4]
    modified=modified1
    modified2=b[-4]
    modified=modified2+modified1
    print(modified)
