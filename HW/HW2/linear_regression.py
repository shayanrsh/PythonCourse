import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats as st


def linear_regression(x=None, y=None, data_set=None):
    if data_set is not None:
        df = pd.read_csv(data_set, nrows=1000)
        df = df.dropna()
        print(df.head())
        if data_set == 'bottle.csv':
            X = df['T_degC']
            X = X.to_numpy()
            Y = df['Salnty']
            Y = Y.to_numpy()
        else:
            X = df.iloc[:, 0]
            X = X.to_numpy()
            Y = df.iloc[:, 1]
            Y = Y.to_numpy()
    else:
        X = x
        Y = y

    # Visualizing the data
    x_label, y_label = df.columns
    plt.scatter(X, Y)
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.show()

    # Adding 1 to the X matrix for the intercept
    one_column = np.ones((X.shape[0], 1))
    X = np.concatenate((one_column, X), axis=1)

    # Beta
    Beta = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))

    # Y_hat
    n = X.shape[1]  #number of obs.
    h = np.ones((X.shape[0], 1))
    theta = Beta.reshape(1, n)
    for i in range(0, X.shape[0]):
        h[i] = float(np.matmul(theta, X[i]))
    regression_estimates = h.reshape(X.shape[0])

    """# number of observations/points
    n = np.size(X)

    # mean of x and y vector
    m_x = np.mean(X)
    m_y = np.mean(Y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(np.dot(Y, X)) - n * m_y * m_x
    SS_xx = np.sum(np.dot(X, X)) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    regression_estimates = b_0 + b_1 * X"""

    # Visualizing the data
    x_label, y_label = df.columns
    plt.scatter(X, Y)
    plt.plot(X, regression_estimates, color='red', linewidth='2')
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.show()

    standard_errors = []
    credible_intervals = []

    return regression_estimates, standard_errors, credible_intervals
