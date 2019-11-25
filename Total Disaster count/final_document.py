import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

# 显示高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

data = Counter([row['State'] for index, row in pd.read_csv('final_document.csv').iterrows()])
xs = data.keys()
ys = data.values()

def autoAdd():
    plt.title('Total disaster from 1953 - 2019 for each State', fontsize=15)
    plt.xlabel('State', fontsize=15)
    plt.ylabel('Count', fontsize=15)

dict = {}
for x,y in zip(xs,ys):
    dict.update({x:y})

xss = sorted(xs,key= lambda i:i[0])

num = int(xss.__len__() / 3)

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

b = 0

for x in xss:
    y = dict.__getitem__(x)
    if 2 * num > b and b > num:
        x2.append(x)
        y2.append(y)
    elif b > 2 * num:
        x3.append(x)
        y3.append(y)
    else:
        x1.append(x)
        y1.append(y)
    b += 1


autolabel(plt.bar(range(len(y1)), y1, color='rgb', tick_label=x1))
autoAdd()
plt.show()

autolabel(plt.bar(range(len(y2)), y2, color='rgb', tick_label=x2))
autoAdd()
plt.show()

autolabel(plt.bar(range(len(y3)), y3, color='rgb', tick_label=x3))
autoAdd()
plt.show()


