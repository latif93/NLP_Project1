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

def find_best_dressed(year):
    tweets = import_json_file(year)
    best_dressed_freq_dict = dict()
    for tweet in tweets:
        if "best dressed" in tweet["text"].lower():
            best_dressed_candidates = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"])
            for best_dressed_candidate in best_dressed_candidates:
                if "best" not in best_dressed_candidate.lower():
                    add_to_freq_dict(best_dressed_candidate, best_dressed_freq_dict)
    best_dressed_freq_dict_sorted_by_highest_freq = sorted(best_dressed_freq_dict.items(), key=lambda x: x[1], reverse=True)  
    return best_dressed_freq_dict_sorted_by_highest_freq[0][0]

