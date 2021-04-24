# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:32:52 2021

@author: Yosshua
"""


import random as rd

n_cases = 10
for i in range(n_cases):
    
    n = int(rd.random()*100)
    fin = []
    for j in range(n):
        ncar = int(rd.random()*100)
        pts = '.'*ncar
        x = 'X'*(100-ncar)
        s = pts+x
        s = (''.join(rd.sample(s,len(s)))+'\n')
        fin.append(s)
    for j in range(100-n):        
        fin.append(('.'*100)+'\n')        
    rd.shuffle(fin)
    w = ""
    for l in fin:
        w+=l
    f = open(str(i)+".in","w")
    f.write("100\n"+w)
    f.close()



