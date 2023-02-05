
import re
import json
import award_hardcoded 

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
        freq_dict[item] +=1
def find_potential_presenters(tweets, awards):
    award_to_presenter_dict = dict()
    for award in awards:
        award_to_presenter_dict[award] = dict()
    for tweet in tweets:
        for award in awards:
            for keyword in award_hardcoded.get_keywords()[award]:
                if "present" in tweet['text'].lower() and keyword in tweet['text'].lower() and keyword != "best":
                    presenters = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"]) 
                    for presenter in presenters:
                        if "best" not in presenter.lower():
                            add_to_freq_dict(presenter, award_to_presenter_dict[award])
    for award in award_to_presenter_dict:
        award_to_presenter_dict[award] = sorted(award_to_presenter_dict[award], key = award_to_presenter_dict[award].get)[::-1][:2]
    return award_to_presenter_dict
def find_presenters(year, awards):
    tweets = import_json_file(year)
    result = find_potential_presenters(tweets, awards)
    return result
