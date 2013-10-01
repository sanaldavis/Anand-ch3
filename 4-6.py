import urllib
import sys
import re

def urlread(url):
  ufile=urllib.urlopen(url)
  f=ufile.info()
  text=ufile.read()
  #print text
  data=re.sub('<.*?>','',text)
  print data
  a=ufile.geturl()
  print a
  b=a.split('/')
  if b[-1]=='':
    urlprint('index.html',data)
  else:
    urlprint(b[-1],data)

def urlprint(fname,text):
  f=open(fname,'w')
  f.write(text)
  f.close()

urlread(sys.argv[1])
