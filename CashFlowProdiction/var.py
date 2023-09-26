import math
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.vector_ar.var_model import VAR
import statsmodels.api as sm
from statsmodels.tsa.vector_ar.vecm import coint_johansen


def demo_var():
    df = pd.read_csv('c:\\shDuoWei6.csv', parse_dates=['ds'])
    df.dtypes
    print(df.dtypes)
    # 时间列加上索引
    # df['ds'] = pd.to_datetime(df.ds, format='%d/%m/%Y')
    data = df.drop(['ds'], axis=1)
    data.index = df.ds

    # 训练数
    # train = data[:int(0.85*(len(data)))]
    train = data[:60]
    # 验证数
    # valid = data[int(0.85*(len(data))):]
    valid = data[48:]

    print(len(train))
    print(train)
    print(len(valid))
    print(valid)

    # 检查平稳性
    # coint_johansen(data, -1, 1).eig

    # 拟合
    model = VAR(endog=train, freq='MS')
    # a = model.select_order(3)
    # print(a.summary())
    # len(train)-5
    model_fit = model.fit(len(train) - 2)
    # print(model_fit.summary())
    # a = model_fit.k_ars
    # print(a)
    prediction = model_fit.forecast(model_fit.endog, steps=len(valid))
    # 图形展示
    fig1 = model_fit.plot_forecast(steps=len(valid))
    cols = data.columns
    pred = pd.DataFrame(index=range(0, len(prediction)), columns=[cols])
    for j in range(0, len(cols)):
        for i in range(0, len(prediction)):
            pred.iloc[i][j] = prediction[i][j]
    # 比较实际和预测差距
    # for i in cols:
    # print('rmse value for', i, 'is : ', sqrt(mean_squared_error(pred[i], valid[i])))

    #
    print(pred)


    # print(valid)

    error = []
    m = 0
    for i in range(len(valid)):
        error.append(valid.iloc[i][3] - pred.iloc[i][3])
        cha = abs(valid.iloc[i][3] - pred.iloc[i][3])
        print("误差百分比：", cha / valid.iloc[i][3])
        m += cha / valid.iloc[i][3]
    print("平均：", m / len(valid))
    print("Errors: ", error)
    print(error)
    squaredError = []
    absError = []
    m = 1
    for val in error:
        squaredError.append(val * val)  # target-prediction之差平方
        absError.append(abs(val))  # 误差绝对值
        # diffrent.append(abs(val)/valid.iloc[i][3])
    print("Square Error: ", squaredError)
    print("Absolute Value of Error: ", absError)
    # 均方误差MSE
    print("MSE = ", sum(squaredError) / len(squaredError))
    # 误差参数
    w = math.log(1 / sum(squaredError))
    print(w)
    # 预测2022年的数据
    model = VAR(endog=data, freq='MS')
    model_fit = model.fit()
    model_fit.plot()
    plt.show()
    yhat = model_fit.forecast(model_fit.endog, steps=12)
    print(yhat)

    # 图形展示
    # fig = model_fit.plot_forecast(steps=12)


if __name__ == '__main__':
    demo_var()
    print('caculate seccused！')