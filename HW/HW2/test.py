# importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def linear_regression(X, Y):
    column_of_ones = np.ones([len(X)], dtype=int)
    X_final = np.stack((column_of_ones, X), axis=-1)

    res1 = np.dot(X_final.T, X_final)
    res2 = np.linalg.inv(res1)
    res3 = np.dot(res2, X_final.T)
    res4 = np.dot(res3, Y)

    plt.figure(figsize=(20, 10))
    plt.scatter(X, Y, c="b", s=5)
    plt.xlabel("SAT Score")
    plt.ylabel("GPA")
    B0 = res4[0]
    B1 = res4[1]
    Y_pred = B0 + B1 * X
    plt.plot(X, Y_pred, color="r")
    plt.show()

    # Sum of Errors
    E = Y - Y_pred
    n = len(Y)
    sse = np.dot(E.T, E) / (n - 2)
    # Standard Errors 
    se = math.sqrt(sse)
    print("Standard Error is: ", se)


x_test = np.array([1, 1])
y_test = np.array([2, 2])
linear_regression(x_test, y_test)
