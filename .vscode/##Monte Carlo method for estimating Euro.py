##Monte Carlo method for estimating European Options.
import numpy as np
import math
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif' 
plt.rcParams['font.serif'] = 'Ubuntu' 
plt.rcParams['font.monospace'] = 'Ubuntu Mono' 
plt.rcParams['font.size'] = 14 
plt.rcParams['axes.labelsize'] = 12 
plt.rcParams['axes.labelweight'] = 'bold' 
plt.rcParams['axes.titlesize'] = 12 
plt.rcParams['xtick.labelsize'] = 12 
plt.rcParams['ytick.labelsize'] = 12 
plt.rcParams['legend.fontsize'] = 12 
plt.rcParams['figure.titlesize'] = 12 
plt.rcParams['image.cmap'] = 'jet' 
plt.rcParams['image.interpolation'] = 'none' 
plt.rcParams['figure.figsize'] = (6, 4) 
plt.rcParams['axes.grid']=True
plt.rcParams['lines.linewidth'] = 2 
plt.rcParams['lines.markersize'] = 8
colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',
'xkcd:scarlet']



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
a=100 * np.exp((0.05-0.2 ** 2 /2)*1 + 0.2 *math.sqrt(1)*z)
b = np.maximum(a-105,0)
q= math.exp(-0.05)*np.mean(b)
gamma = a-100
Alpha = np.mean(gamma)
print(q)
plt.hist(gamma, bins=int(10000/1))
plt.axvline(Alpha,color = 'b')