import json
import re
from data import get_2013_award_data  # had to install requests to run this, do we note this for the TA to run our code?


# This might be useful for the "required output format"
class Award:
    def __init__(self, name, nominees):
        self.name = name
        self.nominees = nominees
        self.winner = ""
        self.presenters = []
        self.aliases = []
        # TODO: ALIASES: for really long category names, maybe just map them to shorter ones that users would type?
        #  example alias: "Best Motion Picture - Drama" --> "Best Drama" ? or something like that
        #  this would have to be hardcoded somehow but idk if it's really necessary


# list of all Award objects and all of their info
all_award_info = []

# TODO: figure out best ways to map short award names tweeted by users to their official award names
awards = ["Best Actor", "Best Actress",  # best actor/actress has 4 subcategories
          "Best Supporting Actress", "Best Supporting Actor",
          "Best Director", "Best Motion Picture",
          "Best Comedy or Musical", "Best Drama",  # best motion picture has 2 subcategories
          "Best Screenplay", "Best Original Song",
          "Best Original Score", "Best TV Series",  # TV has 2 subcategories
          "Best Foreign Language Film", "Best Animated Feature Film",
          "Miss Golden Globe", "Mr. Golden Globe"
          ]


def import_json_file():
    file = open('gg2013.json')
    tweets = json.load(file)
    file.close()
    return tweets


# extracting individual category names from their corresponding nominees and store that info in some structure
# for typechecking.
# Decide between Dictionary(awards, nominees) or List of Award objects? or something else
def extract_and_parse_imdb_data():
    # importing in the mined imdb data
    imdb_data = get_2013_award_data()
    cats_and_noms_str = imdb_data.split("\n\n")  # break up the different categories
    awards_to_noms = dict()  # dictionary to use for typechecking, maps award category to its nominees
    for mapping in cats_and_noms_str:
        mapping = mapping.split("\n")
        category = mapping[0]
        nominees = mapping[1:]

        # TODO: decide on data structure for the type checking, could be either
        #  a dict mapping award categories to nominees, or it could be a
        #  list of Award objects that contain all info about each award. the latter
        #  could be even more useful down the line if we implement award aliasing well enough
        awards_to_noms[category] = nominees
        all_award_info.append(Award(category, nominees))
    # print("Award: " + category + ". \nNominees: " + str(nominees))
    # print()


def add_to_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1


name_matcher = "[A-Z][a-z]* [A-Z][a-z]*"
# TODO: need a better regex matcher for things like movie titles?

# dictionary where each key is an award,
# then each value is another dictionary in which each key is a 'winner' string mapped to frequency
award_to_winners = dict()

# initializes each award key in award_to_winners to have a frequency dictionary as its value
def initialize_winner_dicts():
    for award in awards:
        award_to_winners[award] = dict()


def parse_tweets(tweets):
    for i, tweet in enumerate(tweets):
        tweet_lower = tweet["text"].lower()

        # TODO: think of other phrasings indicative of someone winning something
        # look for some pattern like {award} won by {winner}, needs improvement
        won_by_index = tweet_lower.find("won by")  # might not be a very useful phrase, not a lot of tweets have it??
        if won_by_index != -1:
            for award in award_to_winners:
                if award.lower() in tweet_lower:
                    # TODO: find a better ending point for string slice?
                    winner_match = re.search(name_matcher, tweet["text"][won_by_index:])

                    if winner_match:
                        add_to_dict(winner_match.group(), award_to_winners[award])

        # look for some pattern like {winner} won {award}, needs improvement
        else:
            won_index = tweet_lower.find("won")
            if won_index != -1:
                for award in award_to_winners:
                    if award.lower() in tweet_lower:
                        # TODO: find a better starting point than index 0 so that it can be directly before the won_index?
                        winner_match = re.search(name_matcher, tweet["text"][0:won_index])

                        if winner_match:
                            add_to_dict(winner_match.group(), award_to_winners[award])


# for each award, sort the frequency counts of the potential winners by greatest to least
# but for some reason turns the inner frequency dictionary into a list of tuples but that works i guess
def sort_winner_freqs():
    for award_dict in award_to_winners:
        award_to_winners[award_dict] = sorted(award_to_winners[award_dict].items(), key=lambda x:x[1], reverse=True)

# TODO: typechecking: throw away anyone / any movie that was determined to be a winner but was not a nominee?


# printing the results of what we've determined the winners to be
def print_results():
    for award in award_to_winners.keys():
        if award_to_winners[award]:
            print(award + ", " + str(award_to_winners[award][0]))
        else:
            print(award + ", No results found")


def main():
    tweets = import_json_file()
    extract_and_parse_imdb_data()
    initialize_winner_dicts()
    parse_tweets(tweets)
    sort_winner_freqs()
    print_results()


main()


