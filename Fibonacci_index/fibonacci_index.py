'''
@author: Gopi Vinod Avvari
for more info, see attached documentation
'''

import math

phi = (1+math.sqrt(5))/2  # golden search ratio
tau = (1-math.sqrt(5))/2  # \/phi
N = 100                   # range of test
F = []
eps = pow(10, -10)
for n in range(N):
    F.append((pow(phi, n)-pow(tau, n))/math.sqrt(5))
    print n,
    print F[-1],
    print (pow(phi, n))/math.sqrt(5),
    if F[-1] == 0:
        fibonacci_index = 0
    elif F[-1] == 1:
        fibonacci_index = [1, 2]
    else:
        fibonacci_index = int(round(math.log(F[-1] * math.sqrt(5)+eps) / math.log(phi)))
    print fibonacci_index
