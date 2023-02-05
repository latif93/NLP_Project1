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

    # sorts all key/values in dictionary into a list of tuples: List[ (Name, Vote) ]
    host_freq_dict_sorted_by_highest_freq = sorted(host_freq_dict.items(), key=lambda x: x[1], reverse=True)  #, key = host_freq_dict.get)[::-1]

    # remove top voted host since it is Will Ferrel for some reason
    host_freq_dict_sorted_by_highest_freq = host_freq_dict_sorted_by_highest_freq[1:]

    # autograder expects a list of one or more strings
    actual_hosts = []

    # each potential host from the sorted dict is a tuple: (Name, Votes)
    first_potential_host = host_freq_dict_sorted_by_highest_freq[0]
    second_potential_host = host_freq_dict_sorted_by_highest_freq[1]

    # determine if top two voted 'hosts' were mentioned around the same number of times
    # if the numbers are close, then there actually two hosts.
    # if the numbers are not close at all, then there was only one
    if first_potential_host[1] / second_potential_host[1] < 1.15:  # idk just a random value for a threshold rn
        actual_hosts.append(first_potential_host[0])
        actual_hosts.append(second_potential_host[0])
    else:
        actual_hosts.append(first_potential_host[0])

    return actual_hosts
    # return host_freq_dict_sorted_by_highest_freq[1:] #Remove first item, typically "Golden Globes"
