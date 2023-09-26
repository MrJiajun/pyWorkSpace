
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

df_A = pd.read_csv('c:\\sh.csv', parse_dates=['ds'])
m = Prophet()
m.fit(df_A)
future = m.make_future_dataframe(1, freq='m')
future.tail()
forecast = m.predict(future)
print(forecast.columns)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

# df = pd.DataFrame(forecast)
# df.to_csv("C:\\result.csv")

fig1 = m.plot(forecast)
x1 = forecast['ds']
y1 = forecast['trend']
plt.plot(x1, y1)
plt.show()

