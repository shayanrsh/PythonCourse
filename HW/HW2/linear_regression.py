import numpy as np
import pandas as pd
from numpy.linalg import inv
import matplotlib.pyplot as plt


def linear_regression(x, y):
    left_term = np.dot(x.T, x)
    left_term = inv(left_term)
    middle_term = np.dot(left_term, x.T)
    beta_hat = np.dot(middle_term, y)

    return beta_hat
