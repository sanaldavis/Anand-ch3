import urllib
import re
import sys

def link(url):
  ufile=urllib.urlopen(url)
  a=ufile.read()
  b=re.findall(r'[\w.-]+@[\w.-]+',a)
  print b

link(sys.argv[1])

