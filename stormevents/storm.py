import matplotlib.pyplot as plt
import pandas as pd
import os

def getseries(file):
    df = pd.read_csv(file,sep=',',header=0, usecols=[8],dtype=str)
    s = pd.Series(df[df.columns[0]])
    s = s.value_counts()
    s = s.sort_index()
    return s

def plot(df):
    for state in df.index:
        ax = plt.gca()
        ax.scatter(y=df.loc[state,:],x=df.columns)
        xticks = ([2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
        x = np.linspace(xticks[0], xticks[-1], 10)
        X = sm.add_constant(x)
        model = sm.OLS(df.loc['ALABAMA',:],X)
        results = model.fit()
        y = results.params['x1'] * x + results.params['const']
        plt.plot(xticks, y, linewidth=4, color='red')
    

def main():
    l = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.sort()
    files = files[1:11]

    for file in files:
        s = getseries(file)
        l.append(s)

    d
    df = df.T
    indexname = df[df[2009]<100].index
    df.drop(indexname,inplace=True)
    plot(df)

if __name__ == '__main__':
    main()
