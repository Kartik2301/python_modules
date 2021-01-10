import matplotlib.pyplot as plt
import numpy as np
import urllib
import urllib.request
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import matplotlib.dates as mdates

"""
# lines,labels and legends

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y,label='First Line')
plt.plot(x2,y2, label='Second Line')
# add labels and titles

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('Interesting graph\nCheck it out')
# add legend

plt.legend()

plt.show()
"""









# bar charts and histograms

# bar charts

"""

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x,y,label='Bars 1', color='cyan')
plt.bar(x2,y2,label='Bars 2', color='red')
plt.title('Interesting graph\nCheck it out')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()

"""

# histogram

"""
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
# ids = [x for x in range(len(popluation_ages))]

bins = [0,10,20,40,50,60,70,80,100,110,120,130]

plt.hist(population_ages,bins=bins, histtype='bar', rwidth=0.8,label='hist label')

plt.title('Interesting graph\nCheck it out')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
"""







# scatter plots

"""

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='scatter',color='k', marker='*', s=10)

plt.show()

"""






# stack plots

"""

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m', label='sleeping', linewidth=5)
plt.plot([],[],color='c', label='eating', linewidth=5)
plt.plot([],[],color='r', label='working', linewidth=5)
plt.plot([],[],color='k', label='playing', linewidth=5)
plt.stackplot(days, sleeping,eating,working,playing, colors = ['m','c','r', 'k'])

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

"""







# pie charts

"""

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,2,13]
activities = ['sleeping','eating','eorking','playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%'
        )
plt.title('pie chart')
plt.show()

"""






# loading data from file

# method 1

"""

import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y,label='loaded')
plt.xlabel('x')
plt.ylabel('y')

plt.title('loaded from file')

plt.legend()
plt.show()

"""

# method 2

"""

x,y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x,y,label='loaded')
plt.xlabel('x')
plt.ylabel('y')

plt.title('loaded from file')

plt.legend()
plt.show()


"""






# getting data from internet

"""

def bytespdate2_num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2_num('%Y%m%d')})
    


    plt.plot_date(date,closep)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('loaded from file')
    plt.legend()
    plt.show()

graph_data('TSLA')

"""





# 3d Mapping

"""

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

ax1.plot(x,y,z)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

plt.show()

"""







# 3d scatter plots

"""

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [1,2,6,3,2,7,3,3,7,2]

ax1.scatter(x,y,z,c='g',marker='o')
ax1.scatter(x2,y2,z2,c='r',marker='*')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

plt.show()

"""







# 3d bar charts

"""

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,7,8,2,5,6,3,7,2]
z3 = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x3,y3,z3,dx,dy,dz)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

plt.show()

"""
