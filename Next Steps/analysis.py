import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv('bookdetails.csv')

print(type(dataSet))
print(dataSet)
print(dataSet.describe())
print(dataSet.columns)
print(sum(dataSet['Price']))
print(sum(dataSet['Rating']))
print(dataSet[['Price','Rating']])
print(dataSet['Price'])
print(dataSet[dataSet.Stock.str.contains(r'Out')]['Price'])
print(dataSet[dataSet['Rating']>=4.0][['Title','Price']])
print(dataSet[dataSet.Rating.between(3.5,4.5)]['Title'])

price_group = dataSet[['Price']]
print(price_group)
bar_plot = price_group.plot()
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

price_group = dataSet[['Price']]
bar_plot = price_group.plot(kind='bar')
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

price_group = dataSet[['Price','Rating']]
bar_plot = price_group.plot(kind='bar',title="Book Price and Rating")
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

labels = dataSet[['Stock']]
print(labels)
price_group = dataSet[['Price','Rating']]
bar_plot = price_group.plot(kind='bar',title="Book Price and Rating")
bar_plot.set_xlabel("No of Books")
bar_plot.set_xticklabels(labels)
bar_plot.set_ylabel("Price")
plt.show()
