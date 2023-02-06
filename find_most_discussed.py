import json
import re
import sys

def import_json_file(year):
    filename = f"gg{year}.json"
    try:
        file = open(filename)
        tweets = json.load(file)
        file.close()
        return tweets
    except FileNotFoundError:
        print("Could not find the file " + filename)
        sys.exit()

def add_to_freq_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1

def find_most_discussed(year):
    tweets = import_json_file(year)
    most_discussed_freq_dict = dict()
    for tweet in tweets:
        most_discussed_candidates = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"])
        for most_discussed_candidate in most_discussed_candidates:
            add_to_freq_dict(most_discussed_candidate, most_discussed_freq_dict)
    most_discussed_freq_dict_sorted_by_highest_freq = sorted(most_discussed_freq_dict.items(), key=lambda x: x[1], reverse=True)  
    return most_discussed_freq_dict_sorted_by_highest_freq[1][0]