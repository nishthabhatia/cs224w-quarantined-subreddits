#File that uses psaw, a wrapper for pushshift, to essentially crawl reddit submissions, for a given set of subreddits
#This constructs an edge list, where an edge is between two users if they interacted with eacher other.
from psaw import PushshiftAPI
import datetime as dt
import json


#quarantined_subreddits = ["GentilesUnited", 'watchpeopledie', 'fragilejewishredditor', 'TheRedPill', "cringeanarchy",
#"FullCommunism", "braincels", "Ice_Poseidon", "whitebeauty", "911truth", "Gore",
#"GoyimDefenceForce", "SubOfPeace"]
non_quarantined_subreddits1 = ["announcements", "funny", "AskReddit", "todayilearned", "science", "worldnews", "pics",
"IAmA", "gaming", "videos", "movies", "aww", "Music", "blog", "gifs", "news", "explainlikeimfive", "askscience"]


for i in range(len(quarantined_subreddits)):
    api = PushshiftAPI()
    start_epoch=int(dt.datetime(2018, 7, 8).timestamp())

    comment_id_to_author = {}
    subname = quarantined_subreddits[i]
    gen1 = api.search_submissions(subreddit=subname)

    num_submissions_processed = 0
    for c in gen1:
        comment_id_to_author[c.id] = c.author
        num_submissions_processed += 1
        if num_submissions_processed >= 30000:
            break

    gen = api.search_comments(subreddit=subname)

    #G = snap.PUNGraph.New()
    max_response_cache = 100000
    cache = []
    stringid_to_intid = {}
    num_nodes = 0

    for c in gen:
        cache.append(c)

        # Omit this test to actually return all results. Wouldn't recommend it though: could take a while, but you do you.
        if len(cache) >= max_response_cache:
            break
    for i in range(len(cache)):
        comment_id_to_author[cache[i].id] = cache[i].author
    txtname = "QuarantinedPairs/" + subname + "pairs.txt"
    with open(txtname, 'w') as fil:
        for i in range(len(cache)):
            s = cache[i].parent_id
            s = s[s.find("_")+1:]
            if s in comment_id_to_author:
                parent_author = comment_id_to_author[s]
                fil.write("%s\n" % cache[i].author)
                fil.write("%s\n" % parent_author)
