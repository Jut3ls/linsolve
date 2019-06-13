#!/usr/bin/env python3
"""Contains routines to test the solvers module"""

import numpy as np
import pytest
import solvers


def test_gaussian_eliminate_1():
    """Test gaussian_eliminate-Function"""
    print("\nTest 1")
    a = np.array([[2.0, 4.0, 4.0], [5.0, 4.0, 2.0], [1.0, 2.0, -1.0]])
    b = np.array([1.0, 4.0, 2.0])
    x_expected = np.array([0.666666666666667, 0.416666666666667, -0.5])
    x_gauss = solvers.gaussian_eliminate(a, b)
    assert np.all(np.abs(x_gauss - x_expected) < 1e-10)


def test_gaussian_eliminate_2():
    """Test gaussian_eliminate-Function a second time"""
    print("\nTest 2")
    a = np.array([[2.0, 4.0, 4.0], [1.0, 2.0, -1.0], [5.0, 4.0, 2.0]])
    b = np.array([1.0, 2.0, 4.0])
    x_expected = np.array([0.666666666666667, 0.416666666666667, -0.5])
    x_gauss = solvers.gaussian_eliminate(a, b)
    assert np.all(np.abs(x_gauss - x_expected) < 1e-10)


def test_gaussian_eliminate_3():
    """Test gaussian_eliminate-Function on depedency"""
    print("\nTest 3")
    a = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    b = np.array([1.0, 2.0, 3.0])
    x_expected = None
    x_gauss = solvers.gaussian_eliminate(a, b)
    assert x_expected == x_gauss


if __name__ == '__main__':
    pytest.main()
