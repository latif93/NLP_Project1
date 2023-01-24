import json
import re

file = open('gg2013.json')
tweets = json.load(file)
file.close()


def add_to_dict(item, freq_dict):
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] += 1


# TODO: work with more awards, but remember they can't be hardcoded
awards = ["Best Actor", "Best Supporting Actress", "Best Supporting Actor",
          "Best Actress", "Best Motion Picture", "Best Director"]  # hardcoding awards to make rough draft
winners = dict()

name_matcher = "[A-Z][a-z]* [A-Z][a-z]*"

# dictionary where each key is an award, and then each value is a dictionary mapping strings to freq counts
award_to_winners = dict()
for award in awards:
    award_to_winners[award] = dict()


for i, tweet in enumerate(tweets):
    tweet_lower = tweet["text"].lower()
    won_index = tweet_lower.find("won")  # TODO: maybe use other key words?
    if won_index != -1:
        for award in awards:  # just testing things out with hardcoded values
            if award.lower() in tweet_lower:
                # TODO: find a better starting point than index 0 so that it can be directly before the won_index?
                winner_match = re.search(name_matcher, tweet["text"][0:won_index])
                if winner_match:
                    add_to_dict(winner_match.group(), award_to_winners[award])


# for each award, sort the frequency counts of the potential winners by greatest to least
# but for some reason turns the inner frequency dictionary into a list of tuples but that works i guess
for award_dict in award_to_winners:
    award_to_winners[award_dict] = sorted(award_to_winners[award_dict].items(), key=lambda x:x[1], reverse=True)

# printing the results of what we've determined the winners to be
for award in award_to_winners.keys():
    print(award + ", " + str(award_to_winners[award][0]))






