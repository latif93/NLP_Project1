import re
import json 
import requests
import ast
from data import get_2013_award_data
from data import get_2015_award_data

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
def create_lists_of_potential_nominees(year, tweets, awards):
    award_data = ""
    if year == "2013":
        award_data = get_2013_award_data()
    if year == "2015":
        award_data = get_2015_award_data()
    award_to_nominee_dict = dict()
    nominees_dict = dict()
    award_words = dict()
    for award in awards:
        award_to_nominee_dict[award] = dict()
        if award in award_data.lower():
            nominees_dict[award] = award_data.lower().split(f"{award.lower()}\n")[1].split("\n\n")[0].split("\n")
        award_words[award] = award.split(" ") 
    count = 0
    for tweet in tweets:
        #print(count)
        count += 1
        for award in awards:
            for word in award_words[award]:
                if word in tweet["text"].lower() and word != "-":
                    nominee_names = re.findall("[A-Z][a-z]*[- ]?[A-Z][a-z]*", tweet["text"])
                    for nominee_name in nominee_names:
                #        if award not in nominees_dict:
                #            if len(award_to_nominee_dict[award]) < 7:
                #                add_to_freq_dict(nominee_name, award_to_nominee_dict[award])
                #        else:
                        if award not in nominees_dict:
                            nominees_dict[award] = []
                            add_to_freq_dict(nominee_name, award_to_nominee_dict[award])
                        if nominee_name.lower() in nominees_dict[award]:
                            add_to_freq_dict(nominee_name, award_to_nominee_dict[award])
    for award in award_to_nominee_dict:
        award_to_nominee_dict[award] = sorted(award_to_nominee_dict[award], key = award_to_nominee_dict[award].get)[::-1]
    return award_to_nominee_dict

def find_nominees(year, awards):
    tweets = import_json_file(year)
    award_nominees = create_lists_of_potential_nominees(year, tweets, awards)
    return award_nominees

