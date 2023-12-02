import matplotlib.pyplot as plt  # displays a plot on the screen
import seaborn as sns
from numpy import random

# quick seaborn example
# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()

#--------------------------------Normal Distribution--------------------------------
# x = random.normal(loc=3, scale=2, size=(2, 3))
# print(x)

# sns.distplot(random.normal(loc=10, scale=50, size=1000), hist=False)
# plt.show()

#--------------------------------Binomial Distribution--------------------------------
# x = random.binomial(n=10, p=0.5, size=10000)  # n is number of samples, and p is probability
# print(x)
#
# sns.distplot(x, hist=True, kde=False)
# plt.show()
#
# sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=1000, p=0.05, size=1000), hist=False, label='binomial')
#
# plt.show()

#--------------------------------Poisson Distribution--------------------------------

# x = random.poisson(lam=2, size=10)
# print(x)

# sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
# plt.show()

#--------------------------------Uniform Distribution--------------------------------

# x = random.uniform(size=(2, 3))
#
# print(x)

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
