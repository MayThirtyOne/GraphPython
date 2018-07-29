#Author : Vijay
#Dated :29th July, 2018
#Sample graph plotting with two datasets in Python 3.7
#Required modules: matplotlib,numpy,csv


import matplotlib.pyplot as red
import csv as poo
import numpy as np

x = []
y = []
m = []
n = []

with open('out.txt','r') as csvfile:
    plots = poo.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
with open('equal.txt','r') as csvfile:
    plots = poo.reader(csvfile, delimiter=',')
    for row in plots:
        m.append(int(row[0]))
        n.append(int(row[1]))
red.figure(figsize=(10,2))
red.plot(x,y, label='Input Image')
red.xticks(np.arange(0,255,10))
red.plot(m,n, label='Equalized Image')
red.xlabel('Color Range')
red.ylabel('Frequency')
red.title('PMG Pixels Graph\n-Contrast-')
red.legend()
red.savefig('out.png', dpi=300)
red.savefig('out.pdf', dpi=300)
red.show()
