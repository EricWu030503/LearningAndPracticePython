# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from qids import *
import re
pd.set_option("display.max_rows", None, "display.max_columns", None) #enable to print all the rows and columns
env = make_env()  # initialize the environment

fundamental_df, market_df = env.get_current_market()
print(market_df)
# sample code using random number as prediction
'''
random.seed(42)
while not env.is_end():
    fundamental_df, market_df = env.get_current_market()  # get correlated dataset

# make your prediction Y here and replace the following four rows

    l = []
    for idx in range(54):
        l.append(random.random())
    predict_ds = pd.Series(l)

    env.input_prediction(predict_ds)  # upload your predicted Y

print(pd.read_csv('/Users/owen/Downloads/QIDS/predicted_return.csv'))
'''
