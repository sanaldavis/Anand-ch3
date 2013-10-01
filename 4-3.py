import commands
import re

a=commands.getoutput('ls -l')
b=a.split('\n')
for i in b:
  c=re.sub(' ','	',i)
  #print c,'\n'
  print c[39:],'\n' 


