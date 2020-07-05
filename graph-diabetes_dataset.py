# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:40:19 2020

@author: raylla
"""

from sklearn import datasets
import matplotlib.pyplot as plt

#load the data
diabetes=datasets.load_diabetes()

#you can find more styles to your graph on matplotlib website
plt.style.use('bmh')

plt.title('Graph', loc='left')

#cmap: color gradient
#c: choose the variable which the color will vary
#s: size of points
#alpha: opacity level
plt.scatter(diabetes.data[:,0], diabetes.target, cmap='magma',
            c=diabetes.data[:,3],s=60, alpha=0.7)

plt.axes().set(xlabel='age',ylabel='diabetes')

cbar = plt.colorbar()
cbar.set_label('average blood pressure')

#bbox_inches='tight': will save your figure without cut the edges
#facecolor: you can choose the edge color
#dpi: resolution
plt.savefig('graph-diabetes_dataset.png',
            bbox_inches='tight',facecolor='white',dpi=300)