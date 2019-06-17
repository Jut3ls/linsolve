"""Solves matrix from file input"""

import sys
import solvers
import numpy as np

try:
    fp = open('linsolver.in', 'r')
except FileNotFoundError:
    print("Can not open file {}".format('linsolver.in'))
    print('Exiting...')
    sys.exit(1)
else:
    data = np.loadtxt('linsolver.in', skiprows=1, dtype=float, delimiter=' ')

    array = data[0:3]

    vector = data[3]

    # numstr = fp.readline(1)

    # numval = int(numstr)

    result = solvers.gaussian_eliminate(array, vector)

    if result is None:
        fp = open('linsolver.out', 'w')
        fp.write('ERROR: LINDEP')
        fp.close()
    else:
        np.savetxt('linsolver.out', result)
