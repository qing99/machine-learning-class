'''
A = [[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]]
v = [1 / 3, 1 / 3, 1 / 3]
You can also initialize v to be random positive numbers just needs to sum to 1
Do this loop
do 25 times:
    v' = vA
    v = v'
By the 25the step you've calculated original v times A^25
On each step, plot the Euclidean distance between |v' - v| as a function of iteration
You should notice that it converges to 0
As a quiz, this about what we've just found (in terms of linear algebra)
'''

import numpy as np
import matplotlib as plt

A = np.array([[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]])
    
V = np.array([0.25, 0.25, 0.5])

y = np.array([])
for x in range(0, 25):
     Vdel = V.dot(A)
     y = np.append(y, np.linalg.norm(Vdel - V))
     V = Vdel
     
plt.plot(x, y)
plt.show()
     