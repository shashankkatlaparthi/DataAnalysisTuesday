import matplotlib.pyplot as plt
import pandas as pd
from import_data import d

def analysis_one():
	genres = {}
	for m in d['items']:
		for genre in m['genres'].split('|'):
			if genre not in genres.keys():
				genres[genre] = 1
			else:
				genres[genre] += 1
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	x_ticklables = genres.keys()
	values = genres.values()
	ax.set_title('Number of movies based on genres')
	ax.set_xlabel('Genre')
	ax.set_ylabel('Number of movies')
	ax.set_xticklabels(x_ticklables,rotation=30,fontsize='small')
	data = pd.Series(values, index=x_ticklables)
	data.plot(kind='bar', ax=ax, color='b', alpha=0.7)
	data.plot(kind='line', ax=ax, color='r', alpha=0.7)
	plt.show()

#analysis_one()
