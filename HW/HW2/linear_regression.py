import numpy as np
import pandas as pd
from numpy.linalg import inv
import matplotlib.pyplot as plt


def linear_regression(x=None, y=None, data_set=None):
    df = pd.read_csv(data_set, nrows=1000)
    if data_set == 'bottle.csv':
        x = df['T_degC']
        y = df['Salnty']
    else:
        x = df.columns(0)
        y = df.columns(1)

    # left_term = np.dot(x.T, x)
    # left_term = inv(left_term)
    # middle_term = np.dot(left_term, x.T)
    # beta_hat = np.dot(middle_term, y)

    plt.scatter(x, y)
    plt.show()

    regression_estimates = []
    standard_errors = []
    credible_intervals = []

    return regression_estimates, standard_errors, credible_intervals
