import argparse, os, datetime, requests, json
from requests_oauthlib import OAuth1


def check_folder(newpath):
	if not os.path.exists(newpath):
		os.makedirs(newpath)

def create_file(data, filename):
    statuses = data['statuses']
    json_data = json.dumps(statuses)
    with open(filename+'.json', 'w') as json_file:
        json.dump(statuses,json_file)
    
    

if __name__ == "__main__":
    
    search = 'trump'
    count = 20

    #Take search term from command line using argparse
    parser = argparse.ArgumentParser(description = "Search and save tweets")
    parser.add_argument("-st",dest='search_term',default=search,help="Search Term")
    args = parser.parse_args()
    term = str(args.search_term)

    #Check and create folder structure
    now = datetime.datetime.now()
    path = '_'.join([str(now.year),str(now.month),str(now.day)])
    path = term+'/'+path
    check_folder(path)
    
    #Get relevant tweets
    auth = OAuth1('QkhoFndp1I6eQ3QcwuYQ3OqsP', 'VQY9VQXIzhIdYCSQnapn4XXoFCy04lQRhb0ZwNOcEQrRnFKBtK', '730233993589882881-0zw1ICAawKXtAF463Kw1P4AO61S2mrn', 'pxGqq7m6y3kJnf7saL28pKA7ch4pFuDR4Ex8jtAuGRne1')
    
    print 'Fetching Tweets for '+term
    base_url = 'https://api.twitter.com/1.1/search/tweets.json?q='
    since = '&since='+'-'.join([str(now.year),str(now.month),str(now.day-5)])
    until = '&until='+'-'.join([str(now.year),str(now.month),str(now.day)])
    count = '&count='+str(count)
    get_url = base_url+term+since+until+count
    r = requests.get(get_url, auth=auth)
    tweets_dict = r.json()
    print 'Creating files and saving tweets for '+term+'\n'

    #Save the tweets as json in folder structure
    file_name = path+'/'+':'.join([str(now.hour),str(now.minute),str(now.second)])
    file_name = path+'/'+term
    create_file(tweets_dict, file_name)

    

    
