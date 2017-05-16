# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:39:16 2017

@author: kashu
"""

"""Softmax."""


scores = [[1, 2, 3, 6],
          [2, 4, 5, 6],
          [3, 8, 7, 6]]
                   

import numpy as np
import math as ma


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    y = np.array(x,dtype='f')
    np.array
    if(y.ndim == 1):
        columns = len(y)
        total=0
        for l in range(0,columns):
            total = total + ma.exp(y[l])
            print('total %d',total)
        for m in range(0,columns):
            print('ma.exp %d',ma.exp(y[m]))
            y[m] = float(ma.exp(y[m]))/float(total)
            print(y[m])
        return y

    else:
        rows,columns = y.shape
        s=y
        for l in range(0,columns):
            total=0
           
            for m in range(0,rows):
             
                total = total + ma.exp(y[m][l])
                
            for t in range(0,rows):
                s[t][l] = (ma.exp(y[t][l]))/(total*1.0)
        return y            
        
        
        

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
