from data import get_2013_award_data

# print(get_2013_award_data())

# key: official title
# value: keywords related to title
# TODO: include keywords we should ignore, like "golden" & "globes", or if its a movie, ignore words like "television"

awards_aliasing = {
    "Best Motion Picture - Drama":
        ["best", "drama"],

    "Best Motion Picture - Comedy or Musical":
        ["best", "comedy", "musical"],

    "Best Performance by an Actor in a Motion Picture - Drama":
        ["best", "actor", "drama"],

    "Best Performance by an Actress in a Motion Picture - Drama":
        ["best", "actress", "drama"],

    "Best Performance by an Actor in a Motion Picture - Comedy or Musical":
        ["best", "actor", "comedy", "musical"],

    "Best Performance by an Actress in a Motion Picture - Comedy or Musical":
        ["best", "actress", "comedy", "musical"],

    "Best Performance by an Actor in a Supporting Role in a Motion Picture":
        ["best", "actor", "supporting"],

    "Best Performance by an Actress in a Supporting Role in a Motion Picture":
        ["best", "actress", "supporting"],

    "Best Director - Motion Picture":
        ["best", "director"],

    "Best Screenplay - Motion Picture":
        ["best", "screenplay"],

    "Best Original Song - Motion Picture":
        ["best", "song"],

    "Best Original Score - Motion Picture":
        ["best", "score"],

    # some good results with the stuff from above

    "Best Television Series - Drama":
        ["best", "series", "drama"],

    "Best Television Series - Comedy or Musical":
        ["best", "series", "comedy"],  # idk if checking for musical really matters tbh

    "Best Performance by an Actor in a Television Series - Drama":
        ["best", "actor", "series", "drama"],

    "Best Performance by an Actress in a Television Series - Drama":
        ["best", "actress", "series", "drama"],

    "Best Performance by an Actor in a Television Series - Comedy or Musical":
        ["best", "actor", "series", "comedy"],

    "Best Performance by an Actress in a Television Series - Comedy or Musical":
        ["best", "actress", "series", "comedy"],

    "Best Performance by an Actor in a Supporting Role in a Series, Miniseries or Motion Picture Made for Television":
        ["best", "actor", "supporting", "series"],

    "Best Performance by an Actress in a Supporting Role in a Series, Miniseries or Motion Picture Made for Television":
        ["best", "actress", "supporting", "series"],

    "Best Performance by an Actor in a Miniseries or Motion Picture Made for Television":
        ["best", "actor", "series"],

    "Best Performance by an Actress in a Miniseries or Motion Picture Made for Television":
        ["best", "actress", "series"],

    "Best Animated Feature Film":
        ["best", "animation"],  # animated vs animation

    "Best Foreign Language Film":
        ["best", "foreign"],

    "Best Miniseries or Motion Picture Made for Television":
        ["best", "miniseries"]

}


def get_keywords():
    return awards_aliasing
