import argparse, os, requests, json
from operator import itemgetter

def check_folder(newpath):
	if not os.path.exists(newpath):
		os.makedirs(newpath)

def create_json_file(data, filename):
    with open(filename+'.json', 'w') as json_file:
        json.dump(data,json_file)
    
def read_json_file(filename):
  with open(filename+'.json', 'r') as json_file:
    data = json.load(json_file)
  return data

#****************************************analysis one****************************************#

def analysis_one_save_data():  
  path = 'Analysis_1/'
  
  #To get questions tagged python and pandas
  url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=python%3Bpandas&site=stackoverflow'
  r = requests.get(url)
  output = r.json()

  #To check if folder exists and save above response in questions.json
  if 'error_message' not in output.keys():
    check_folder(path)
    path_questions = path+'questions'
    create_json_file(output, path_questions)

  #For each user in the questions, do the following
  for item in output['items']:
    #Get user_id
    user_id = item['owner']['user_id']

    #Get badges information for user_id
    url = 'https://api.stackexchange.com/2.2/users/'+str(user_id)+'/badges?order=desc&sort=rank&site=stackoverflow'
    r = requests.get(url)
    badges_info = r.json()

    #save it in a file with name user_id
    path_badges = path+str(user_id)
    create_json_file(badges_info, path_badges)

def analysis_one_parse_data():
  user_id_questions_name = {}
  badge_value = {'gold':3,'silver':2,'bronze':1}
  user_weightage = {}
  path = 'Analysis_1/'

  #Read questions from file
  filename = path+'questions'
  output = read_json_file(filename)

  #To save user_id and questions
  for i in output['items']:
    user_id_questions_name[i['owner']['user_id']]=(i['title'],i['owner']['display_name'])

  #To get user with maximum weightage
  max_weight = 0
  for user in user_id_questions_name.keys():
    filename = path+str(user)
    output = read_json_file(filename)
    user_weightage[user]=0
    for badge in output['items']:
      user_weightage[user] += badge_value[badge['rank']]
    if user_weightage[user] > max_weight:
      max_weight = user_weightage[user]
      max_weight_user = user

  return user_id_questions_name[max_weight_user]

def analysis_one():
  print 'Getting data'
  analysis_one_save_data()
  print 'Parsing data'
  user_id_questions_name = analysis_one_parse_data()
  print '\nTop question based on weightage is:'
  print user_id_questions_name[0]
  print '\nPosted by: ',user_id_questions_name[1]

#****************************************analysis two****************************************#

def analysis_two_save_data():
  path = 'Analysis_1/'
  
  filename = path+'questions'
  output = read_json_file(filename)
  
  path = 'Analysis_2/user_tags/'
  check_folder(path)
  for item in output['items']:
    user_id = item['owner']['user_id']
    url = 'https://api.stackexchange.com/2.2/users/'+str(user_id)+'/tags?order=desc&sort=popular&site=stackoverflow'
    r = requests.get(url)
    user_tags_data = r.json()

    path_user_tags = path+str(user_id)
    create_json_file(user_tags_data, path_user_tags)


def analysis_two_parse_data():
  tags_to_users = {}
  path = 'Analysis_1/'
  
  filename = path+'questions'
  output = read_json_file(filename)
  
  path = 'Analysis_2/user_tags/'
  
  for item in output['items']:
    user_id = item['owner']['user_id']
    user_tags_data = read_json_file(path+str(user_id))
    for i in user_tags_data['items']:
      if i['name'] not in tags_to_users.keys():
        tags_to_users[i['name']] = [item['owner']]
      else:
        tags_to_users[i['name']].append(item['owner'])

  path = 'Analysis_2/tags_sorted/'
  check_folder(path)
  for i in tags_to_users.keys():
    sorted_list = sorted(tags_to_users[i], key=itemgetter('reputation'))[::-1]
    user_info = ''
    for j in sorted_list:
      try:
        user_info += str(j['reputation']) + '\t\t'
        user_info += str(j['user_id']) + '\t\t\t'
        user_info += str(j['display_name']) + '\t\t\t\t'
        user_info += str(j['link']) + '\n'
      except:
        continue
      
    filename = path+str(i)
    with open(filename+'.txt', 'w') as text_file:
        text_file.write(user_info)

def analysis_two():
  print 'Getting data'
  analysis_two_save_data()
  print 'Saving data in Analysis_2/tags_sorted'
  analysis_two_parse_data()

#****************************************analysis three****************************************#
      
def analysis_three():
  badge_numbers = {'gold':0,'silver':0,'bronze':0}
  
  path = 'Analysis_1/'
  filename = path+'questions'
  output = read_json_file(filename)
  for item in output['items']:
    user_id = item['owner']['user_id']
    user_tags_data = read_json_file(path+str(user_id))
    for i in user_tags_data['items']:
      badge_numbers[i['rank']] +=1
  
  for i in badge_numbers:
    print 'Users having '+i+' bagde = '+str(badge_numbers[i])

#****************************************analysis four****************************************#

def analysis_four():
  all_tags = {}

  path = 'Analysis_1/'
  
  filename = path+'questions'
  questions = read_json_file(filename)

  for q in questions['items']:

    for tag in q['tags']:
      if tag not in all_tags.keys():
        all_tags[tag] = [1,q['answer_count']]

      else:
        all_tags[tag][0] += 1
        all_tags[tag][1] += q['answer_count']
  
  for i in all_tags.keys():
    print 'For the tag: ',i
    print 'Number of questions asked = ',all_tags[i][0]
    print 'Number of answers to all the questions = ',all_tags[i][1],'\n'


#****************************************analysis five****************************************#

def analysis_five_save_data():
  path = 'Analysis_1/'
  filename = path+'questions'
  output = read_json_file(filename)

  check_folder('User_Questions/')
  
  for item in output['items']:
    path = 'User_Questions/'
    user_id = item['owner']['user_id']
    url = 'https://api.stackexchange.com/2.2/users/'+str(user_id)+'/questions?order=desc&sort=activity&site=stackoverflow'
    r = requests.get(url)
    user_questions = r.json()
    path_user_questions = path+str(user_id)
    create_json_file(user_questions, path_user_questions)

def analysis_five_parse_data():
  path = 'Analysis_1/'
  filename = path+'questions'
  output = read_json_file(filename)
  path = 'User_Questions/'
  min_vote_count = 9999999
  for item in output['items']:
    user_id = item['owner']['user_id']
    filename = path+str(user_id)
    user_questions = read_json_file(filename)
    score = 0
    for q in user_questions['items']:
      score += q['score']
    if score < min_vote_count:
      min_vote_count = score
      min_vote_count_user = item['owner']['display_name']
  return min_vote_count_user, score

def analysis_five():
  analysis_five_save_data()
  user, count = analysis_five_parse_data()
  print 'User with lowest vote count is ',user
  print 'Vote count = ',count

#****************************************end of analysis five****************************************#



an = str(raw_input('Enter analysis number you want to run: ')).lower()
if (an == 'one' or an == '1'):
  analysis_one()
elif (an == 'two' or an == '2'):
  #analysis_one_save_data()
  analysis_two()
elif (an == 'three' or an == '3'):
  #analysis_one_save_data()
  analysis_three()
elif (an == 'four' or an == '4'):
  #analysis_one_save_data()
  analysis_four()
elif (an == 'five' or an == '5'):
  #analysis_one_save_data()
  analysis_five()
else:
  print 'Invalid argument. Please enter value between 1 and 5'
