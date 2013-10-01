import commands
import re

def extcnt():
  a=commands.getoutput('ls')
  #print a
  w=re.findall('\.\w+',a)
  #print w
  cnt={}
  for i in w:
    if i in cnt:
      cnt[i]=cnt[i]+1
    else:
      cnt.setdefault(i,1)
  print cnt.items()
extcnt()
