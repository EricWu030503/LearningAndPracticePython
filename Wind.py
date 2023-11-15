import pandas as pd
import numpy as np
from WindPy import *
import matplotlib.pyplot as plot
pd.set_option('display.max_rows',None,'display.max_columns',None)
w.start()
#print(w.wsd("3690.HK", "CLOSE", "2022-02-05", "2023-02-05",usedf=True))
historical_data=w.wsd("3690.HK", "CLOSE", "2022-02-05", "2023-02-05").Data[0]
log_daily_ratio=[]
previous_price=historical_data[0]
for price in historical_data:
    log_daily_ratio.append(np.log(price/previous_price))
    previous_price=price
log_daily_ratio.pop(0)
hv_5=[]
dates_5=w.wsd("3690.HK", "CLOSE", "2022-02-12", "2023-02-05").Times
for i in range(len(log_daily_ratio)-4):
    hv_5.append(np.std(log_daily_ratio[i:i+5]))
hv_15=[]
dates_15=w.wsd("3690.HK", "CLOSE", "2022-02-26", "2023-02-05").Times
for i in range(len(log_daily_ratio)-14):
    hv_15.append(np.std(log_daily_ratio[i:i+15]))
hv_30=[]
dates_30=w.wsd("3690.HK", "CLOSE", "2022-03-19", "2023-02-05").Times
for i in range(len(log_daily_ratio)-29):
    hv_30.append(np.std(log_daily_ratio[i:i+30]))
plot.plot(dates_5,hv_5,label="HV5")
plot.plot(dates_15,hv_15,label="HV15")
plot.plot(dates_30,hv_30,label="HV30")
plot.title("Historical Volatility for Meituan(3690.HK)")
plot.xlabel("Dates")
plot.ylabel("Historical Volatility")
plot.legend()
plot.show()
#print(f'The historical volatility is: {np.std(daily_return)*100}%')




