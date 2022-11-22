#import python reddit api wrapper
import praw
import pandas as pd
#create an instance of the reddit class
#here one would paste in the client id, client secret, username, and password
reddit = praw.Reddit(client_id='info',
                        client_secret='info',
                        username='info',
                        password='info',
                        user_agent='info')
                        
#secret: 0niAopa_2msvDwEYw5tkJ6MeZa4h7g
#define a subreddit to search
subreddit = reddit.subreddit('wallstreetbets')
#use the hot signifier to return the top 5 posts
hot_python = subreddit.hot(limit = 5)
title = []
PostID = []
timeCreated = []
comments = []
i = 0
j = 0
for submission in hot_python:
    timeCreated.append(submission.created_utc)
    PostID.append(submission.id)
    title.append(submission.title)
    for comment in submission.comments:
        if submission.comments is not None:
            submission.comments.replace_more(limit=0)
            comments.append(comment.body)
            
    i += 1

df = pd.DataFrame({'PostID':PostID, 'Title':title, 'TimeCreated':timeCreated})
commentsdf = pd.DataFrame({'Comments':comments})
print(commentsdf.head())