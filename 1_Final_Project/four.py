import matplotlib.pyplot as plt
import pandas as pd
from import_data import d

def analysis_four():
	# actor = {'Name of actor' : [sum of IMDB scores, number of movies]}
	actor = {'Chris Hemsworth':[0,0], 
		'Christian Bale':[0,0],
		'Johnny Depp':[0,0],
		'Robert Downey Jr.':[0,0],
		'Leonardo DiCaprio':[0,0]}
	for m in d['items']:
		if m['actor_1_name'] in actor.keys():
			actor[m['actor_1_name']][0] += float(m['imdb_score'])
			actor[m['actor_1_name']][1] += 1
		if m['actor_2_name'] in actor.keys():
			actor[m['actor_2_name']][0] += float(m['imdb_score'])
			actor[m['actor_2_name']][1] += 1
		if m['actor_3_name'] in actor.keys():
			actor[m['actor_3_name']][0] += float(m['imdb_score'])
			actor[m['actor_3_name']][1] += 1
	
	actor_average = {}
	for a in actor.keys():
		actor_average[a] = actor[a][0]/actor[a][1]
	
	figure = plt.figure()
	ax = figure.add_subplot(1, 1, 1)
	x_ticklables = [e+1 for e in range(len(actor_average.keys()))]
	values = actor_average.values()
	ax.set_title('Average IMDB Scores of Actors')
	ax.set_xlabel('Actors')
	ax.set_ylabel('IMDB Score')
	
	count = 0
	for actor, value in actor_average.items():
		ax.annotate(actor, xy=(count, value), xytext=(count, value+0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
		count += 1

	ax.set_xticklabels(x_ticklables,fontsize='small')
	data = pd.Series(values, index=x_ticklables)
	data.plot(kind='bar', ax=ax, color='b', alpha=0.7)
	plt.show()

#analysis_four()
