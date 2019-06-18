# change
# another change
"""Routines for solving a linear system of equations."""
import numpy as np


def gaussian_eliminate(aa, bb):
    """Solves a linear system of equations (Ax = b) by Gauss-elimination

    Args:
        aa: Matrix with the coefficients. Shape: (n, n).
        bb: Right hand side of the equation. Shape: (n,)

    Returns:
        Vector xx with the solution of the linear equation or None
        if the equations are linearly dependent.
    """
    nn = aa.shape[0]
    xx = np.zeros((nn,), dtype=float)
    """Solving Matrix with partial pivoting"""
    cc = np.array(aa)
    for j in range(0, nn):
        y = cc[j:, j]  # array contains columns of aa
        z = np.argmax(y) + j  # z looks for row-position of highest abs val in column
        for i in range(j+1, nn):
            temp = np.array(aa[z])
            temp2 = np.array(bb[z])
            # swapping rows of aa and bb
            if aa[i-1, j] != 0:  # only performs shift if first entry of row isn't zero
                aa[z], aa[i-1] = aa[i-1], temp
                bb[z], bb[i-1] = bb[i-1], temp2
            if aa[i, j] == 0:
                continue
            bb[i] = aa[j, j] / aa[i, j] * bb[i] - bb[j]
            aa[i] = aa[j, j] / aa[i, j] * aa[i] - aa[j]

    """Solution-Vector"""
    for k in range(nn-1, -1, -1):
        for g in range(nn-1, k, -1):
            bb[k] = bb[k] - aa[k, g] * xx[g]
        if aa[k, k] == 0:
            continue
        xx[k] = bb[k] / aa[k, k]

    # trying to catch the linear dependency
    for t in range(0, nn):
        if np.all(aa[t] == 0):
            if abs(xx[t]) == 0:
                return None

    return xx
#test for