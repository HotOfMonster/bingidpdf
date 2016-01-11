#! /usr/bin/env python
import os,sys

f=open(sys.argv[1])
for line in f:
  line=line.strip()
  if (len(line)>4):
    bdir="bid/"+line[:4]
    if not os.path.exists(bdir):os.makedirs(bdir)
    fw=open(bdir+line+".html",'w')
    fw.write("<html>ok</html>")
    fw.close()
