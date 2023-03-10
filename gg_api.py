'''Version 0.35'''
import find_winners
import find_awards
import find_nominees
import find_hosts
import find_presenters
import find_best_dressed
import find_worst_dressed
import find_most_discussed
import json
import sys

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    hosts = find_hosts.find_hosts(year)
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    awards = find_awards.find_awards(year)[0:25]
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    nominees = find_nominees.find_nominees(year, OFFICIAL_AWARDS_1315)
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    winners = {}
    found = find_winners.return_winners(year)
    for award_obj in found:
        autograder_category = award_obj.name.lower()
        winner = award_obj.winner
        winners[autograder_category] = winner

    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    presenters = find_presenters.find_presenters(year, OFFICIAL_AWARDS_1315)
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    # I think this would be the general structure for the required JSON output stuff
    # But it's not done / idk where it belongs / idk what we're basing it all off of.
    year = sys.argv[1]
    awards = get_awards(year)
    nominees = get_nominees(year)
    hosts = get_hosts(year)
    presenters = get_presenters(year)
    best_dressed = find_best_dressed.find_best_dressed(year)
    worst_dressed = find_worst_dressed.find_worst_dressed(year)
    most_discussed = find_most_discussed.find_most_discussed(year)
    readable_results = f"Host(s): {hosts}\n\n"

    results = {"Host(s)": hosts}
    for won_award in find_winners.return_winners(year):
        won_award.nominees = nominees[won_award.name.lower()]
        won_award.presenters = presenters[won_award.name.lower()]
        readable_results += f"Award: {won_award.name}\nPresenters: {won_award.presenters}\nNominees: {won_award.nominees}\nWinner: {won_award.winner}\n\n"
        results[won_award.name] = {"Presenters": won_award.presenters,
                              "Nominees": won_award.nominees,
                              "Winner": won_award.winner}
    readable_results += f"Best Dressed: {best_dressed}\nWorst Dressed: {worst_dressed}\nMost Discussed: {most_discussed}"
    json_result = json.dumps(results)
    print(json_result)
    print(readable_results)

    return

if __name__ == '__main__':
    main()
