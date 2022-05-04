data {
  int n;
  vector[n] x;
}

parameters {
  vector<lower=0, upper=1>[n] mu;
  vector<lower=0>[2] kappa;
}

model {
  // https://mc-stan.org/docs/2_22/functions-reference/beta-proportion-distribution.html
  mu[1] ~ beta(1, 1);
  kappa ~ gamma(5, 1);
  x[1] ~ beta_proportion(mu[1], kappa[1]);
  for (t in 2:n) {
    mu[t] ~ beta_proportion(mu[t - 1], kappa[2]);
    x[t] ~ beta_proportion(mu[t], kappa[1]);
  }
}

