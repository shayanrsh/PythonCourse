import numpy as np
import pandas as pd
import math
import scipy.stats as st


def linear_regression(x=None, y=None, data_set=None):
    if data_set is not None:
        df = pd.read_csv(data_set, nrows=1000)
        df = df.dropna()
        print(df.head())
        if data_set == 'modified_bottle.csv':
            X = df[['T_degC', 'Depthm']]
            X = X.to_numpy()
            Y = df['Salnty']
            Y = Y.to_numpy()
        else:
            X = df.iloc[:, 0:1]
            X = X.to_numpy()
            Y = df.iloc[:, 2]
            Y = Y.to_numpy()
    else:
        X = x
        Y = y

    # one is added to X for further calculations
    modified_X = np.concatenate((np.ones((len(X), 1), dtype=int), X), axis=1)

    beta_hat = np.linalg.solve(np.dot(modified_X.T, modified_X), np.dot(modified_X.T, Y))
    print("Coefficients: ", beta_hat.reshape(beta_hat.shape[0], ).tolist())

    regression_estimates = np.dot(modified_X, beta_hat)

    error = Y - regression_estimates
    standard_errors = math.sqrt(np.dot(error.T, error) / (len(Y) - X.shape[1]))

    standard_errors_var = np.sqrt(np.diag(np.dot(error.T, error) / (len(Y) - X.shape[1]) *
                                          np.linalg.inv(np.dot(modified_X.T, modified_X)))).tolist()

    beta_list = beta_hat.reshape(beta_hat.shape[0], ).tolist()

    # Dictionary of beta - standard_errors tuples to be used in the CI formula
    beta_without_se_dict = dict(zip(beta_list, standard_errors_var))

    # %95 Confidence Intervals
    t_statistic = st.t.ppf(1 - 0.025, len(Y) - X.shape[1])

    # Lower CI's
    lower_CI = []
    for beta in beta_without_se_dict:
        lower_CI.append(beta - (t_statistic * beta_without_se_dict[beta]))

    # Upper CI's
    upper_CI = []
    for beta in beta_without_se_dict:
        upper_CI.append(beta + (t_statistic * beta_without_se_dict[beta]))

    credible_intervals = [lower_CI, upper_CI]

    t_statistic_list = []
    # intercept t_statistic-value
    for beta in beta_without_se_dict:
        t_statistic_list.append(beta / beta_without_se_dict[beta])
    print("t_statistic-values: ", t_statistic_list)

    for t_statistic_value in t_statistic_list:
        if t_statistic_value < t_statistic:
            print("Failed to reject the null hypothesis.")
        else:
            print('Null hypothesis rejected.')

    return regression_estimates, standard_errors, credible_intervals, X, Y
