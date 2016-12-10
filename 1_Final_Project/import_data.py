import argparse, os, datetime, requests, json, operator, pdb
#import matplotlib.pyplot as plt
#import pandas as pd

def check_folder(newpath):
	if not os.path.exists(newpath):
		os.makedirs(newpath)

def create_json_file(data, filename):
    with open(filename+'.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True, separators=(',', ':'))
    
def read_json_file(filename):
  with open(filename+'.json', 'r') as json_file:
    data = json.load(json_file)
  return data

def title_str(title):
	a = title.__repr__()
	val = a.split("'")[1].split('\\')[0]
	return str(val)

def profit(movie):
	try: 
		profit = int(movie['gross']) - int(movie['budget'])
		return profit
	except:	
		return None

d = read_json_file('movie_data')

