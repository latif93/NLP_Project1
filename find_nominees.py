import re
import json 
import requests
import ast
from  data import get_2013_award_data
from  data import get_2015_award_data


file = open('gg2013.json')
tweets = json.load(file)
file.close()

award_data_2013 = get_2013_award_data()
print(award_data_2013)
def add_to_freq_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1

awards = ["Best Performance by an Actress in a Television Series - Drama", "Best Performance by an Actress in a Miniseries or Motion Picture Made for Television", "Best Animated Feature Film"] #hardcoding some awards to make a rough draft using

award_to_nominee_dict = dict()
nominees_dict = dict()
award_words = dict()
for award in awards:
    award_to_nominee_dict[award] = dict()
    nominees_dict[award] = award_data_2013.split(f"{award}\n")[1].split("\n\n")[0].split("\n")
    award_words[award] = award.split(" ") 
print(award_words)
for tweet in tweets:
    for award in awards:
    	for word in award_words[award]:
	        if word in tweet["text"]:
	            nominee_names = re.findall("[A-Z][a-z]*[- ]?[A-Z][a-z]*", tweet["text"])

	            for nominee_name in nominee_names:
	            	if nominee_name in nominees_dict[award]:
	                    add_to_freq_dict(nominee_name, award_to_nominee_dict[award])

for award in award_to_nominee_dict:
    award_to_nominee_dict[award] = sorted(award_to_nominee_dict[award], key = award_to_nominee_dict[award].get)[::-1]

print(award_to_nominee_dict)
