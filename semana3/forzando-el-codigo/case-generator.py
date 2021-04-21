# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:00:12 2021

@author: Yosshua
"""
import random
num = 8
c = "cero"
n = "uno"
for i in range(num):
    nc = int(random.random()*1000)
    nn  = 10000-nc
    s = c*nc+n*nn
    fin = ''.join(random.sample(s,len(s)))
    f = open(str(i+2)+".in","w")
    f.write(fin)
    f.close()
    
