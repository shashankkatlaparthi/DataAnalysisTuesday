import argparse, os, datetime, json

def analysis_one(search_list):
	for i in search_list:
		avg = get_avg_friends(i)
		print 'Average friends for people tweeting about '+i+' = ',avg

def get_avg_friends(term):
	now = datetime.datetime.now()
	path = '_'.join([str(now.year),str(now.month),str(now.day)])
	path = term+'/'+path
	file_name = path+'/'+term
	with open(file_name+'.json', 'r') as json_file:
		statuses = json.load(json_file)
	avg = 0.0
	n = 0
	for i in statuses:
		n += 1
		avg += i['user']['friends_count']
	avg = avg/n
	return avg


def analysis_three(term):
	now = datetime.datetime.now()
	path = '_'.join([str(now.year),str(now.month),str(now.day)])
	path = term+'/'+path
	file_name = path+'/'+term
	with open(file_name+'.json', 'r') as json_file:
		statuses = json.load(json_file)
	return_list = []
	d = statuses[:]
	for _ in range(10):
		val = 0
		for i in d:
			if i['retweet_count'] > val:
				val = i['retweet_count']
				index = i
		return_list.append(index)
		d.remove(index)
	return return_list


if __name__ == "__main__":
	
	#Take search term from command line using argparse
	parser = argparse.ArgumentParser(description = "Run one of five analysis")
	parser.add_argument("-an",dest='an',default=1,help="Analysis Number")
	args = parser.parse_args()
	analysis_num = int(args.an)

	if analysis_num == 1:
		search_list = []
		num = int(raw_input('Enter number of terms you want to search for = '))
		for i in range(num):
			term = str(raw_input('Enter search term #'+str(i+1)+' = '))
			os.system('python Script1.py -st '+term)
			search_list.append(term)

		term = search_list[0]
		analysis_one(search_list)
	
	elif analysis_num == 3:
		term = str(raw_input('Enter the search term = '))
		os.system('python Script1.py -st '+term)
		small = []
		top_retweets = analysis_three(term)
		for i in top_retweets:
			small.append((i['text'],i['retweet_count']))
		print '\nTop 10 Retweeted Tweets for '+term+':\n'
		for i in small:
			print 'Tweet = \n',i[0],
			print '\nRetweet Count = ',i[1]
			print

	else:
		print 'Wrong argument. Please try 1 or 3'











