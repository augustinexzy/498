import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def getseries(file):
    df = pd.read_csv(file,sep=',',header=0, usecols=[8],dtype=str)
    s = pd.Series(df[df.columns[0]])
    s = s.value_counts()
    s = s.sort_index()
    return s

def plots(df):
    for state in df.index:
        ax = plt.gca()
        ax.scatter(y=df.loc[state,:],x=df.columns,label='Data')
        xticks = ([2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
        x = np.linspace(xticks[0], xticks[-1], 15)
        X = sm.add_constant(x)
        model = sm.OLS(df.loc[state,:],X)
        results = model.fit()
        y = results.params['x1'] * x + results.params['const']
        plt.plot(xticks, y, linewidth=4, color='red', label="Linear")
        ax.set_title(r'Stormevents in ' + state + ' from 2004 to 2018 & Prediction for next five years', fontsize=16)
        ax.set_ylabel(r'Numbers of Stormevents occured', fontsize=18)
        ax.set_xlabel(r'Year', fontsize=18)
        prstd, iv_l, iv_u = wls_prediction_std(results)
        ax.plot(x, iv_u, 'r--')
        ax.plot(x, iv_l, 'r--')
        x1n = np.linspace(2019,2023,5)
        Xnew = sm.add_constant(x1n)
        ynewpred =  results.predict(Xnew)
        newxticks = np.hstack((x,x1n))
        newxticks = newxticks.astype(int)
        ax.plot(newxticks, np.hstack((y, ynewpred)), 'g', label="OLS prediction")
        ax.set_xticks(newxticks)
        ax.legend(loc="best");
        plt.show()
    

def main():
    l = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.sort()
    files = files[1:16]
    for file in files:
        s = getseries(file)
        l.append(s)
    df = pd.DataFrame(l,[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
    df = df.T
    indexname = df[df[2004]<100].index
    df.drop(indexname,inplace=True)
    plots(df)

if __name__ == '__main__':
    main()
