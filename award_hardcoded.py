from data import get_2013_award_data

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

# Autograder result from using this algorithm along w gg_api.py hardcoded awards:
# 'winner': {'spelling': 0.6554487179487178}

# words to look for when parsing a tweet for an award.
# Example: for 'best motion picture - drama', most people will write it as 'best drama'.
# so in a dictionary, map the official award name to the keywords that people would use.
# 'best motion picture - drama' : ['best', 'drama']
special_keywords = ['best', 'actor', 'actress', 'supporting',
                    'drama', 'comedy', 'musical',
                    'director', 'screenplay'
                    'song', 'score', 'series',
                    'animated', 'foreign', 'cecil', 'demille']


# key: official title, per the autograder award list in gg_api.py
# value: keywords related to title
# TODO: include keywords we should ignore, like "golden" & "globes", or if its a movie, ignore words like "television"
awards_aliasing2 = {}
for award in OFFICIAL_AWARDS_1315:
    award_keywords = [k for k in special_keywords if k in award]
    awards_aliasing2[award] = award_keywords


def get_keywords():
    return awards_aliasing2

#
#
# Autograder result from my old hardcoded imdb data mechanism
# 'winner': {'spelling': 0.6153846153846154}
#
