import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linear_regression import *

data = pd.read_csv(r'C:\Users\shaya\Desktop\house_price_data.txt', header=None, index_col=False)

data = np.array(data)

print(data)
# plt.figure()
# plt.scatter(data[0], data[2])
# plt.show()

x = np.array(data[0])
# print(x)
y = np.array(data[2])
# print(y)

print(x)
print(np.transpose(x))

# t = linear_regression(x, y)
# print(t)
