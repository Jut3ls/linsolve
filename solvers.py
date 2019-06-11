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
    """Solving Matrix"""
    cc = np.array(aa)
    # print(cc)
    for j in range(0, nn):
        # z needs shift to output proper position of row in aa
        y = cc[j:, j]
        z = np.argmax(y) + j  # shift done here not sure if correct
        # print(y, z)
        for i in range(j+1, nn):
            # setting up temporary variable for pivot
            temp = np.array(aa[z])
            # performing pivot, doesnt seem to be working yet
            # aa might not be properly overwritten by the pivot while solving
            aa[z], aa[i] = aa[i], temp
            # print(temp)
            if aa[i, j] == 0:
                continue
            bb[i] = aa[j, j] / aa[i, j] * bb[i] - bb[j]
            aa[i] = aa[j, j] / aa[i, j] * aa[i] - aa[j]
    """Solution-Vector"""
    xx = np.zeros((nn,), dtype=float)
    for k in reversed(range(0, nn)):
        for g in reversed(range(k+1, nn)):
            bb[k] = bb[k] - aa[k, g] * xx[g]
        if aa[k, k] == 0:
            continue
        xx[k] = bb[k] / aa[k, k]
    return xx


if __name__ == "__main__":
    aa = np.array([[2.0, 4.0, 4.0], [5.0, 4.0, 2.0], [1.0, 2.0, -1.0]])
    dd = np.array([[2.0, 4.0, 4.0], [1.0, 2.0, -1.0], [5.0, 4.0, 2.0]])
    bb = np.array([1.0, 4.0, 2.0])

    xx = gaussian_eliminate(dd, bb)
    # print(xx)
