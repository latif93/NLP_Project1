import json
import re

file = open('gg2013.json')
tweets = json.load(file)
file.close()

def add_to_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] +=1

award_matcher = "Best (.*?) [a-z]" #matches a phrase where Best is followed by capitalized words until a non-capitalized one is found
awards_freq_dict = dict()

for i, tweet in enumerate(tweets):
    match_obj = re.search(award_matcher, tweet["text"])
    if "best" in tweet["text"].lower() and match_obj:
        add_to_dict(match_obj.group(), awards_freq_dict) #filling award frequency dictionary
awards_freq_dict_sorted_by_highest_freq = sorted(awards_freq_dict, key = awards_freq_dict.get)[::-1]

final_awards_lst = []
duplicate_lst = []
for award in awards_freq_dict_sorted_by_highest_freq[0:50]: 
    if award[-2] == " ":
        award = award[0:-2] #fixing formatting of strings
    if award.upper() not in duplicate_lst: #weeding out duplicates with different cases (i.e "Best picture and Best Picture")
        duplicate_lst.append(award.upper())
        final_awards_lst.append(award)    
print(final_awards_lst)
#There are somehwere between 25-30 awards and we have a lot of false positives right now
#------------------------Experimention with hosts--------------------------------------
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


