
import math
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.varmax import VARMAX
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
from statsmodels.tsa.vector_ar.vecm import coint_johansen

df = pd.read_csv('c:\\shDuoWei4.csv', parse_dates=['ds'])
df.dtypes
print(df.dtypes)
# 时间列加上索引
# df['ds'] = pd.to_datetime(df.ds, format='%d/%m/%Y')
data = df.drop(['ds'], axis=1)
data.index = df.ds

# 训练数
train = data[:int(0.85*(len(data)))]
# 验证数
valid = data[int(0.85*(len(data))):]

# varma
model = VARMAX(train, order=(1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.forecast(steps=6)
print(yhat)

# ARIMA
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(train), len(train), typ='levels')
print(yhat)
