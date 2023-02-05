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

def find_hosts(year):
    tweets = import_json_file(year)
    host_freq_dict = dict()
    for tweet in tweets:
        if "host" in tweet["text"]:
            hosts = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"])
            for host in hosts:
                add_to_freq_dict(host, host_freq_dict)
    host_freq_dict_sorted_by_highest_freq = sorted(host_freq_dict, key = host_freq_dict.get)[::-1]
    return host_freq_dict_sorted_by_highest_freq[1:] #Remove first item, typically "Golden Globes"
