import re
import json
import sys 
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

def create_lists_of_potential_presenters(year, tweets, awards):
    award_data = ""
    if year == "2013":
        award_data = get_2013_award_data()
    if year == "2015":
        award_data = get_2015_award_data()
    award_to_presenter_dict = dict()
    presenters_dict = dict()
    award_words = dict()
    for award in awards:
        award_to_presenter_dict[award] = dict()
        if award in award_data.lower():
            presenters_dict[award] = award_data.lower().split(f"{award.lower()}\n")[1].split("\n\n")[0].split("\n")
        award_words[award] = award.split(" ") 
    count = 0
    for tweet in tweets:
        count += 1
        for award in awards:
            for word in award_words[award]:
                if word in tweet["text"].lower() and word != "-":
                    presenter_names = re.findall("[A-Z][a-z]*[- ]?[A-Z][a-z]*", tweet["text"])
                    for presenter_name in presenter_names:
                        if award not in presenters_dict:
                            presenters_dict[award] = []
                            add_to_freq_dict(presenter_name, award_to_presenter_dict[award])
                        if presenter_name.lower() in presenters_dict[award]:
                            add_to_freq_dict(presenter_name, award_to_presenter_dict[award])
    for award in award_to_presenter_dict:
        award_to_presenter_dict[award] = sorted(award_to_presenter_dict[award], key = award_to_presenter_dict[award].get)[::-1]
    return award_to_presenter_dict

def find_presenters(year, awards):
    tweets = import_json_file(year)
    award_presenters = create_lists_of_potential_presenters(year, tweets, awards)
    return award_presenters