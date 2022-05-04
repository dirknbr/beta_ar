
# beta ar process
# https://cran.r-project.org/web/packages/betareg/vignettes/betareg.pdf

import numpy as np
import matplotlib.pyplot as plt
import stan
import arviz
from scipy.special import beta

n = 100
x = np.ones(n) * .1
x[50:] += .5
plt.plot(x)
plt.savefig('plot1.png')

def beta_prop(theta, mu, kappa):
  return (theta ** (mu * kappa - 1)) * ((1 - theta) ** ((1 - mu) * kappa - 1)) / beta(mu * kappa, (1 - mu) * kappa)

theta = np.linspace(.1, .9, 100)
dens = beta_prop(theta, .6, 10)
dens /= sum(dens)
# get the mean
print(sum(dens * theta))

plt.clf()
plt.plot(theta, dens)
plt.savefig('plot2.png')

data = {'n': n, 'x': x}
stancode = open('beta_ar.stan').read()
model = stan.build(stancode, data=data)
fit = model.sample(num_samples=500, num_chains=2)
trace = arviz.from_pystan(fit)
print(arviz.summary(trace))

mu = fit['mu'].mean(axis=1)
plt.clf()
plt.plot(x)
plt.plot(mu)
plt.savefig('plot3.png')
