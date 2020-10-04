from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

year=[2001,2002,2003,2004,2005,2006,2007,2008,2009]
drink_sales=[20000,23000,18000,25000,30000,32000,34000,36000,37000]
plt.bar(year,drink_sales, Label='Drink')
plt.title('product sales over a year in the city')
plt.xlabel('years')
plt.ylabel('sales of drink bottles')
plt.legend()
plt.tight_layout()
plt.show()