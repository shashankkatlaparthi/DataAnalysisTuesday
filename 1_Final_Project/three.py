import matplotlib.pyplot as plt
import pandas as pd
from import_data import d, profit

def analysis_three():
	countries = {}
	for m in d['items']:
		if m['country'] not in countries.keys() and profit(m) != None:
			countries[m['country']] = profit(m)/1000000.0
		elif profit(m) != None:
			countries[m['country']] += profit(m)/1000000.0
	#print countries
	figure = plt.figure()
	ax = figure.add_subplot(1, 1, 1)
	x_ticklables = [e for e in range(len(countries.keys()))]
	values = countries.values()
	ax.set_title('Profit/Loss based on countires')
	ax.set_xlabel('Countries')
	ax.set_ylabel('Profit/Loss (in $mn)')

	count = 0
	for countries, value in countries.items():
		ax.annotate(countries, 
			xy=(count, value), 
			xytext=(count-0.25, 57000),
            rotation = 90
            )
		count += 1

	ax.set_xticklabels(x_ticklables,rotation=0,fontsize='small')
	data = pd.Series(values, index=x_ticklables)
	data.plot(kind='bar', ax=ax, color='b', alpha=0.7)
	plt.show()

#analysis_three()
