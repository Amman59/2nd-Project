#trying API's and Machine Learning 
from sklearn.svm import NuSVC
import numpy as np
import pandas as pd
#import eikon as ek 

data = pd.read_csv('../../source/tr_eikon_eod_data.csv', index_col=0 , parse_dates= True)
data = pd.DataFrame(data['AAPL.0'])
data['returns']= np.log(data/ data.shift())
data.dropna(inplace = True)

lags = 6
cols= []
for lag in range(1,lags+1) : 
    col = 'lag_{}'.format(lag)
    data[col] = np.sign(data['returns'].shift(lag))
    cols.append(col)
data.dropna(inplace = True)



model = NuSVC(gamma='auto')
model.fit(data[cols],np.sign(data['returns']))

data['Prediction']=model.predict(data[cols])
data['Strategy']= data['Prediction']* data['returns']
data[['returns','Srategy']].cumsum().apply(np.exp).plot(figsize=(10,6));