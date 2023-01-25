import re
import json 
import requests
import ast
from  data import get_2013_award_data


file = open('gg2013.json')
tweets = json.load(file)
file.close()


print(get_2013_award_data())
def add_to_freq_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1

awards = ["Best Performance by an Actor in a Motion Picture", "Best Supporting Actress", "Best Motion Picture"] #hardcoding some awards to make a rough draft using

award_to_nominee_dict = dict()

for award in awards:
    award_to_nominee_dict[award] = dict()
for tweet in tweets:
    for award in awards:
        if award in tweet["text"]:
            nominee_names = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"])
            for nominee_name in nominee_names:
                add_to_freq_dict(nominee_name, award_to_nominee_dict[award])

for award in award_to_nominee_dict:
    award_to_nominee_dict[award] = sorted(award_to_nominee_dict[award], key = award_to_nominee_dict[award].get)[::-1]

#print(award_to_nominee_dict)
