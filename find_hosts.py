import re
import json
file = open('gg2013.json')
tweets = json.load(file)
file.close()

def add_to_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] +=1
        
host_freq_dict  = dict()

for tweet in tweets:
    if "host" in tweet["text"]:
        hosts = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"]) 
        #find all strings where two capitalized words are together in tweets with the word "host" in them
        for host in hosts:
        	add_to_dict(host, host_freq_dict) #filling host frequency dictionary
host_freq_dict_sorted_by_highest_freq = sorted(host_freq_dict, key = host_freq_dict.get)[::-1]
print(host_freq_dict_sorted_by_highest_freq[0:5]) 
#Will Ferrel is first for some reason, although second and third place where the real hosts. Gotta think about optimization here.