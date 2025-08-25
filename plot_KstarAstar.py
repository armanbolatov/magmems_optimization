import matplotlib.pyplot as plt
import numpy as np

delta = 0.001
xrange = np.arange(0.01, 3.001, delta)
yrange = np.arange(0.01, 1, delta)
X, Y = np.meshgrid(xrange,yrange)

"Function of A* in terms of ξ"
F = np.sqrt(X*X*(1-Y)*(1-Y)+1)*(2-Y)/(2-2*Y)-(np.arctanh(1/np.sqrt(X*X*(1-Y)*(1-Y)+1))-X*Y/2+np.sqrt(1+X*X)-np.arctanh(1/np.sqrt(1+X*X)))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

"Function of K* in terms of ξ and calculated A* from ξ"

cnt1=ax1.contour(X, Y, F, [0], colors='k', linestyles='dashed')
cnt2=ax2.contour(X, Y/((X*X*(1-Y))/np.sqrt(X*X*(1-Y)*(1-Y)+1)+1/((1-Y)*np.sqrt(X*X*(1-Y)*(1-Y)+1))-X), F, [0], colors='k')

"Plot Two Functions"

import matplotlib.pyplot as plt
import numpy as np

delta = 0.001
xrange = np.arange(0.01, 3.001, delta)
yrange = np.arange(0.01, 1, delta)
X, Y = np.meshgrid(xrange,yrange)

"Function of A* in terms of ξ"
F = np.sqrt(X*X*(1-Y)*(1-Y)+1)*(2-Y)/(2-2*Y)-(np.arctanh(1/np.sqrt(X*X*(1-Y)*(1-Y)+1))-X*Y/2+np.sqrt(1+X*X)-np.arctanh(1/np.sqrt(1+X*X)))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1

"Function of K* in terms of ξ and calculated A* from ξ"

cnt1=ax1.contour(X, Y, F, [0], colors='k', linestyles='dashed')
cnt2=ax2.contour(X, Y/((X*X*(1-Y))/np.sqrt(X*X*(1-Y)*(1-Y)+1)+1/((1-Y)*np.sqrt(X*X*(1-Y)*(1-Y)+1))-X), F, [0], colors='k')


"Plot Two Functions"

ax1.grid()
plt.xticks([0,0.25,0.50,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3])

ax1.set_yticks([0,0.10,0.2,0.30,0.4,0.50,0.6,0.7,0.8,0.9,1])
ax2.set_yticks([0,0.10,0.2,0.30,0.4,0.50,0.6,0.7,0.8,0.9,1])

ax1.set_xlabel('ξ')
ax1.set_ylabel('$K_ξ^*$')
ax2.set_ylabel('$A_ξ^*$')

# evenly sampled time at 200ms intervals
t = np.arange(0., 3., 0.01)
# approximate separatrix
# 1. Define the function
def separatrix_approx(x):
    A = 0.71533
    return (1-A)*A*np.sqrt((x**2)*((1-A)**2)+1)/((x**2)*((1-A)**2)+1-x*(1-A)*np.sqrt((x**2)*((1-A)**2)+1))
    #return (1-A)*A+(1-A)**2*A*x+0.5*(1-A)*(A**2-2*A+1)*A*x**2
    
# blue dashed line
separatrix_line = ax3.plot(t, separatrix_approx(t), 'b--', label='$\\tilde{K}_\\xi^*$')

artists, labels = cnt1.legend_elements()
ax1.legend(artists, ['$A_ξ^*$'], loc = 'upper right')

artists, labels = cnt2.legend_elements()
# Combine the contour legend with the separatrix line legend
handles = artists + separatrix_line
labels_combined = ['$K_ξ^*$'] + ['$\\tilde{K}_\\xi^*$']
ax2.legend(handles, labels_combined, loc = 'upper left')


plt.text(1.85, 0.4, "Periodic solutions", fontsize=12, color='k',
             horizontalalignment='center')

plt.savefig('figs/graph_NN.pdf', dpi=360)
plt.show()