
import re
import json
import award_hardcoded
import sys

# before improvements
# 'presenters': {'completeness': 0.051923076923076926,
#                          'spelling': 0.10180995475113122},

# after presents index
# 'presenters': {'completeness': 0.15, 'spelling': 0.17152149321266966},

# after present index
# 'presenters': {'completeness': 0.3282051282051282,
#                          'spelling': 0.4407522624434389},

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
        tweet_lower = tweet['text'].lower()

        # {person} presents {award}
        presents_index = tweet_lower.find("presents")

        # {multiple people} present {award}
        present_index = tweet_lower.find("present")

        # {award} presented by {person}
        presented_by_index = tweet_lower.find("presented by")

        if presents_index != -1:
            for award in awards:
                award_keywords = award_hardcoded.get_keywords()[award]
                if (award.lower() in tweet_lower) or all(word in tweet_lower for word in award_keywords):
                    presenter_match = re.search("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"][0:presents_index])
                    if presenter_match:
                        add_to_freq_dict(presenter_match.group(), award_to_presenter_dict[award])

        if present_index != -1 and presents_index == -1 and presented_by_index == -1:
            for award in awards:
                award_keywords = award_hardcoded.get_keywords()[award]
                if (award.lower() in tweet_lower) or all(word in tweet_lower for word in award_keywords):
                    presenters_match = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"][0:present_index])
                    for presenter in presenters_match:
                        add_to_freq_dict(presenter, award_to_presenter_dict[award])

        if presented_by_index != -1:
            for award in awards:
                award_keywords = award_hardcoded.get_keywords()[award]
                if (award.lower() in tweet_lower) or all(word in tweet_lower for word in award_keywords):
                    presenters_match = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"][presented_by_index:])
                    for presenter in presenters_match:
                        add_to_freq_dict(presenter, award_to_presenter_dict[award])

            # for keyword in award_hardcoded.get_keywords()[award]:
            #     if "present" in tweet['text'].lower() and keyword in tweet['text'].lower() and keyword != "best":
            #         presenters = re.findall("[A-Z][a-z]* [A-Z][a-z]*", tweet["text"])
            #         for presenter in presenters:
            #             if "best" not in presenter.lower():
            #                 add_to_freq_dict(presenter, award_to_presenter_dict[award])

    # for a in award_to_presenter_dict:
    #     print("award: " + a + ". presenters: " + str(award_to_presenter_dict[a]))
    #     print()

    for award in award_to_presenter_dict:
        award_to_presenter_dict[award] = sorted(award_to_presenter_dict[award], key = award_to_presenter_dict[award].get)[::-1][:2]
    return award_to_presenter_dict

def find_presenters(year, awards):
    tweets = import_json_file(year)
    result = find_potential_presenters(tweets, awards)
    return result
