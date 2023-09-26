import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from random import random
# contrived dataset
# data = [x + random() for x in range(1, 100)]

df = pd.read_csv('c:\\sh1.csv', parse_dates=['ds'])
data = df.drop(['ds'], axis=1)
data.index = df.ds

# 训练数
train = data[:int(0.85*(len(data)))]
# 验证数
valid = data[int(0.85*(len(data))):]

print(np.array(data))
print(data.values.tolist())
# fit model
model = SimpleExpSmoothing(train)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict('2020-07-01', '2020-12-01')
print(yhat)