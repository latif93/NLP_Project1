import re
import json
file = open('gg2013.json')
tweets = json.load(file)
file.close()
#this is bad so far, just quickly whipped something together before leaving
def add_to_freq_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] +=1

awards = ["Best Actor", "Best Supporting Actress", "Best Supporting Actor"] #hardcoding some awards to make a rough draft using
presenter_freq_dict = dict()
for tweet in tweets:
	if "presenter" in tweet['text']:
		presenters = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"]) 
		for presenter in presenters:
		    add_to_freq_dict(presenter, presenter_freq_dict)
presenter_freq_dict_sorted_by_highest_freq = sorted(presenter_freq_dict, key = presenter_freq_dict.get)[::-1]
print(presenter_freq_dict_sorted_by_highest_freq)



