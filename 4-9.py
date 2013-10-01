import re
import sys

def phno(fname):
  f=open(fname,'r')
  a=f.read()
  
  print a
  b=re.findall(r'[+91]?[0]?\d+',a)
  for i in b:
    if i[0]=='+' and len(i)==13:
      print i
    elif i[0]=='0' and len(i)==11:
      print i
    elif len(i)==10:
      print i

phno('phno.txt')
