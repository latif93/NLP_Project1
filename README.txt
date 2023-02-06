Link to our GitHub repo:
https://github.com/latif93/NLP_Project1


Packages to download:
"requests" --> run the command "python3 -m pip install requests"

Instructions:
Running the autograder will run all of our code for scoring.
Running "python3 gg_api.py {year}" will also run all of our code, AND output the results:
  - The first output to stdout is the JSON-compatible format.
  - The second output to stdout is the human-readable format.

We assume the tweet data filenames will maintain the format "gg{year}.json"

Our additional goals:
In addition to the minimum requirements, we note the best dressed, worst dressed, and most discussed people of the ceremony.

* Note: if you do not provide a year argument when calling gg_api.py, it will not work
* Note: We have a get_awards() algorithm to parse the tweets for award names on our own, but we also separately hardcode
        award names for our winners, nominees, and presenters, per the project specifications regarding cascading error.