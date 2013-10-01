import urllib
import sys

def urlread(url):
  ufile=urllib.urlopen(url)
  f=ufile.info()
  text=ufile.read()
  print text
  a=ufile.geturl()
  print a
  b=a.split('/')
  if b[-1]=='':
    urlprint('index.html',text)
  else:
    urlprint(b[-1],text)

def urlprint(fname,text):
  f=open(fname,'w')
  f.write(text)
  f.close()

urlread(sys.argv[1])
