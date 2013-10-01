import re
import sys

def slug(fname):
  f=open(fname,'r')
  a=f.read()
  b=re.findall('\w+',a)
  #type(b)
  c='-'.join(b)
  print c
   

slug(sys.argv[0])
