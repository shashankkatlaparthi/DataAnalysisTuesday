import operator
import matplotlib.pyplot as plt
import pandas as pd
from import_data import d, title_str

def analysis_two(user_input):
	genres = {}

	for m in d['items']:
		title = title_str(m['movie_title'])
		for genre in m['genres'].split('|'):
			try:
				if genre not in genres.keys():
					genres[genre] = {title:int(m['gross'])}
				else:
					genres[genre][title] = int(m['gross'])
			except:
				pass
	
	user_input = int(user_input)
	genre = sorted(genres.keys())[user_input-1]
	sorted_genre = sorted(genres[genre].items(), key=operator.itemgetter(1))[::-1]
	sorted_genre = sorted_genre[:5]
	#print sorted_genre
	x_ticklables = []
	values = []
	for i in range(len(sorted_genre)):
		x_ticklables.append('#'+str(i+1))
		if sorted_genre[i][1]>1000000:
			flag = True
			values.append(sorted_genre[i][1]/1000000)
		else:
			flag = False
			values.append(sorted_genre[i][1])

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.set_title('Top Grossing '+genre+' Movies')
	ax.set_xlabel('Top Movies')
	if flag:
		ax.set_ylabel('Gross (in $mn)')
	else:
		ax.set_ylabel('Gross (in $)')

	names = []
	for i in sorted_genre:
		names.append(i[0])

	for i in range(len(values)):
		ax.annotate(names[i], 
            xy=(i, values[i]), 
			xytext=(i-0.25, values[i]+5),
			size='small')
		
	ax.set_xticklabels(x_ticklables,rotation=30,fontsize='small')
	data = pd.Series(values, index=x_ticklables)
	data.plot(kind='bar', ax=ax, color='b', alpha=0.7)
	#data.plot(kind='line', ax=ax, color='r', alpha=0.7)
	plt.show()

#analysis_two()
