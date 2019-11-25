import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

def parse(df):
    datas = []
    num = 0
    temp = 2018
    list = df['State']

    for i in range(9736):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1953: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data*5:(data+1)*5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])

def first_plot(date, value):
    plt.figure(figsize=(14, 8), dpi=80)
    plt.plot(date, value)
    plt.xticks(rotation=90)
    plt.grid(alpha=0.4)
    plt.title('The number of disasters over time', fontsize=15)
    plt.xlabel('Year', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    for a, b in zip(date, value):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=15)

    plt.show()


def second_plot(datas):
    dates = []
    num = []
    for i in range(len(datas)):
        for j in datas[i].keys():
            dates.append(j)
            print(dates)
        for k in datas[i].values():
            num.append(k)
            print(num)
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(num, dates)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()

def main():
    df = pd.read_csv('Flood.csv')
    date, value, datas = parse(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Flood.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()
    # second_plot(datas)


def parse2(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(438):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1972: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data*5:(data+1)*5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])

def main2():
    df = pd.read_csv('CoastalStorm.csv')
    date, value, datas = parse2(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('CoastalStorm.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()

def parse3(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(438):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1963: 5})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data*5:(data+1)*5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])

def main3():
    df = pd.read_csv('Drought.csv')
    date, value, datas = parse3(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Drought.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()

def parse4(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(111):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data*5:(data+1)*5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])

def main4():
    df = pd.read_csv('Earthquake.csv')
    date, value, datas = parse4(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Earthquake.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()

def parse5(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(2659):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1953: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data*5:(data+1)*5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])

def main5():
    df = pd.read_csv('Fire.csv')
    date, value, datas = parse5(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Fire.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()


def parse6(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(301):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1971: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main6():
    df = pd.read_csv('Freezing.csv')
    date, value, datas = parse6(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Freezing.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()



def parse7(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(10165):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main7():
    df = pd.read_csv('Hurricane.csv')
    date, value, datas = parse7(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Hurricane.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()



def parse8(df):
    datas = []
    num = 0
    temp = 2017
    for i in range(1990):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main8():
    df = pd.read_csv('SevereIceStorm.csv')
    date, value, datas = parse8(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('SevereIceStorm.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()



def parse9(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(16125):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main9():
    df = pd.read_csv('SevereStorm(s).csv')
    date, value, datas = parse9(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('SevereStorm(s).csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()



def parse10(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(3659):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main10():
    df = pd.read_csv('Snow.csv')
    date, value, datas = parse10(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Snow.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()



def parse11(df):
    datas = []
    num = 0
    temp = 2019
    for i in range(1433):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main11():
    df = pd.read_csv('Tornado.csv')
    date, value, datas = parse11(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Tornado.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()



def parse12(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(134):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main12():
    df = pd.read_csv('Typhoon.csv')
    date, value, datas = parse12(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Typhoon.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()

def parse13(df):
    datas = []
    num = 0
    temp = 2018
    for i in range(297):
        if int(df['Incident Begin Date'][i][:4]) == temp:
            num += 1
        else:
            datas.append({temp: num})
            temp = int(df['Incident Begin Date'][i][:4])
            num = 0
    datas.append({1954: 4})
    split_date = []
    split_value = []
    for data in range(int(len(datas) / 5) + 1):
        infos = datas[data * 5:(data + 1) * 5]
        for i in infos[0]:
            end = i
        for i in infos[-1]:
            start = i
        date = (str(start) + '~' + str(end))
        split_date.append(date)

        values = 0
        for info in infos:
            for i in info.values():
                value = int(i)
            values += value
        split_value.append(values)

    return (split_date[::-1], split_value[::-1], datas[::-1])


def main13():
    df = pd.read_csv('Other.csv')
    date, value, datas = parse13(df)
    first_plot(date, value)
    data = Counter([row['State'] for index, row in pd.read_csv('Other.csv').iterrows()])
    x = data.keys()
    y = data.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('The number of disasters per year', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Frenquency', fontsize=15)
    plt.show()


if __name__ == '__main__':
    main()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
    main9()
    main10()
    main11()
    main12()
    main13()