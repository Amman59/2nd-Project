##Monte Carlo method for estimating European Options.
import numpy as np
import math
S0 =100. #Index Value
K= 105. #Strike price of option
T= 1.0 #Time up until maturity
r=0.05 #riskless rate of short
sigma = 0.2 #Volatility
I =1000000 #No. of trials
np.random.seed(1000)
z= np.random.standard_normal(I)
ST = S0 * np.exp((r-sigma ** 2 /2)*T + sigma * math.sqrt(T)*z)
hT = np.maximum(ST-K,0) # payoff at maturity
C0 = math.exp(-r*T)*np.mean(hT) # Monte Carlo Estimator
print('The value of the European call option is : {:5.3f}.'.format(C0))