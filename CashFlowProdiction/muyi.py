

import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

df_A = pd.read_csv('c:\\sh1.csv', parse_dates=['ds'])
m = Prophet()
m.fit(df_A)
future = m.make_future_dataframe(periods=7, freq='m')
future.tail()
forecast = m.predict(future)
print(forecast.columns)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast).show()
m.plot_components(forecast).show()


# forecast[['trend','yearly','yearly_lower','yearly_upper']].tail()
# x1 = forecast['ds']
# y1 = forecast['trend']
# y1 = forecast['yearly']
# plt.plot(x1, y1)
plt.show()