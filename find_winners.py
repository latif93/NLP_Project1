import json
import re

from data import get_2013_award_data  # had to install requests to run this, do we note this for the TA to run our code?
from award_hardcoded import get_keywords  # hardcoded Award names, mapped to their keywords


# This might be useful for the "required output format"
class Award:
    def __init__(self, name, nominees, keywords):
        self.name = name
        self.nominees = nominees
        self.winner = ""
        self.presenters = []
        self.keywords = keywords

    def __str__(self):
        return "Award: " + self.name + "\n  Winner: " + self.winner


# list of all Award objects and all of their info
all_award_info = []


def import_json_file():
    file = open('gg2013.json')
    tweets = json.load(file)
    file.close()
    return tweets


# extracting individual category names from their corresponding nominees and store that info in list of all awards
def extract_and_parse_imdb_data():
    # importing in the mined imdb data
    imdb_data = get_2013_award_data()
    cats_and_noms_str = imdb_data.split("\n\n")  # break up the different categories

    for mapping in cats_and_noms_str:
        mapping = mapping.split("\n")
        category = mapping[0]
        nominees = mapping[1:]

        if category:  # for some reason a final parsed category comes up as '', so just ignore it
            keywords = get_keywords()[category]
            all_award_info.append(Award(category, nominees, keywords))

    # print("Award: " + category + ". \nNominees: " + str(nominees))
    # print()


def add_to_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1


name_matcher = "[A-Z][a-z]* [A-Z][a-z]*"
# TODO: need a better regex matcher for other things like movie/show titles? for ex, Homeland is one of the winners
#  but never comes up rn because it is only one word

# TODO: find a way to exclude words like "golden" or "globes" from being counted as a winner match

# dictionary where each key is an award,
# then each value is another dictionary in which each key is a 'winner' string mapped to frequency
award_to_winners = dict()


# initializes each award key in award_to_winners to have a frequency dictionary as its value
def initialize_winner_dicts():
    for award in all_award_info:   # awards:
        award_to_winners[award.name] = dict()


def parse_tweets(tweets):
    for i, tweet in enumerate(tweets):
        tweet_lower = tweet["text"].lower()

        # TODO: think of other phrasings indicative of someone winning something?
        # look for some pattern like {award} goes to {winner}, needs improvement
        goes_to_index = tweet_lower.find("goes to")
        if goes_to_index != -1:
            for award in all_award_info:
                if (award.name.lower() in tweet_lower) or all(word in tweet_lower for word in award.keywords):
                    # TODO: find a better ending point for string slice?
                    winner_match = re.search(name_matcher, tweet["text"][goes_to_index:])

                    if winner_match:
                        add_to_dict(winner_match.group(), award_to_winners[award.name])

        # look for some pattern like {winner} won {award}, needs improvement
        else:
            won_index = tweet_lower.find("won")
            if won_index != -1:
                for award in all_award_info:
                    # if full award name in tweet (very unlikely) or if all the alias keywords related to that award
                    # are in the tweet
                    if (award.name.lower() in tweet_lower) or all(word in tweet_lower for word in award.keywords):
                        # TODO: find a better starting point than index 0 so that it can be directly before the won_index?
                        winner_match = re.search(name_matcher, tweet["text"][0:won_index])
                        if winner_match:
                            add_to_dict(winner_match.group(), award_to_winners[award.name])


# for each award, sort the frequency counts of the potential winners by greatest to least
# but for some reason turns the inner frequency dictionary into a list of tuples but that works I guess
def sort_winner_freqs():
    for award_dict in award_to_winners:
        award_to_winners[award_dict] = sorted(award_to_winners[award_dict].items(), key=lambda x: x[1], reverse=True)


# for each award, set its winner to the most frequently mentioned winner that was also a nominee
def winner_typechecker():
    for i, award in enumerate(award_to_winners.keys()):
        potential_winner_index = 0
        potential_winner = ""
        nominees = all_award_info[i].nominees

        while potential_winner not in nominees and potential_winner_index < len(award_to_winners[award]):
            potential_winner = award_to_winners[award][potential_winner_index][0]
            potential_winner_index += 1

        all_award_info[i].winner = potential_winner


# printing the results of what we've determined the winners to be
def print_results():
    for award in all_award_info:
        print(award)
        print()

    # for award in award_to_winners.keys():
    #     if award_to_winners[award]:
    #         print(award + ", " + str(award_to_winners[award][0]))
    #     else:
    #         print(award + ", No results found")


def main():
    tweets = import_json_file()
    extract_and_parse_imdb_data()
    initialize_winner_dicts()
    parse_tweets(tweets)
    sort_winner_freqs()
    winner_typechecker()
    print_results()


main()
