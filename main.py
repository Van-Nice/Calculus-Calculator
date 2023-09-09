import latexify as lt
from sympy import *
import sympy as sp
import math
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1/ (1 + math.exp(-x))

output = lt.get_latex(sigmoid)
plt.plot()

a = r'f(x) = \frac{\exp(-x^2/2)}{\sqrt{2*\pi}}'
ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
# ax.set_xticks([])
# ax.set_yticks([])
ax.axis('off')
plt.text(1,1,'$%s$' %output,size=25,color="green")
plt.show()