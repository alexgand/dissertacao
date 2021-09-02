import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
%matplotlib

n = 10
mean = np.random.randint(0,10, size=n)

cov = 

data = np.random.multivariate_normal(mean, cov, size=n, check_valid='warn', tol=1e-8)


mean = [0, 10]

cov = [[1, 20], [10, 20]] 

x, y = np.random.multivariate_normal(mean, cov, 5000).T

plt.plot(x, y, 'x')

plt.axis('equal')

plt.show()