import requests

def sentiment(sentence):
    #import urllib.request as r
    import json
    dic=dict()
    dic["text"]=sentence
    senti=json.loads(requests.post("http://text-processing.com/api/sentiment/",dic).text)
    return senti
def get_comments(IDL):
    reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='')
    submission = reddit.submission(IDL)
    from praw.models import MoreComments
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]  # Seed with top-level
    while comment_queue:
        comment = comment_queue.pop(0)
        print(comment.body,sentiment(comment.body)["label"])
        comment_queue.extend(comment.replies)
    for i in comment_queue:
        print(i)
   
def reddit_scrapper(url, num, after = None):
    
    
    posts = []
    # loop through the num pages, each subreddit .json returns 25 posts 
    for page in range(num):
        # initiate params modifier for posts if there no defined after
        if after == None:
            params = {}
        # add in after id for each loop following to ensure no duplicate posts
        else:
            params = {'after': after}
        # call our get request for the posts
        res = requests.get(url, params=params)
        # check status code, 200 means posts were successfully downloaded
        if res.status_code == 200:
            # convert request to .json
            new_json = res.json()
            # extend list from the 'children' dictionary for each request
            posts.extend(new_json['data']['children'])
            # update after id
            after = new_json['data']['after']
        else:
            # print status code if not 200
            print(res.status_code)
            break
        # wait 1 second
        time.sleep(1)
        
    # create a new dataframe with the 'data' from each post
    new_df = pd.DataFrame([post['data'] for post in posts])
    
    # print final value of after
    print(f'Final value of after parameter: {after}')
    
    # return the dataframe
    return new_df
#3Nl9Q_a8GR0p_g
#	2R4HP3mzTKKOHgjG5Ztas99IW20
import praw
import requests,time
import pandas as pd
reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='sportsapp', \
                     username='', \
                     password='')
subreddit = reddit.subreddit('IndianFootball')
top_subreddit = subreddit.top(limit=100)
print(top_subreddit)
c=[]
for submission in subreddit.top():
    c.append((submission.title, submission.id))
    
    #pass
#data=reddit_scrapper("https://www.reddit.com/r/IndianFootball/",10)
get_comments('dmwypp')
