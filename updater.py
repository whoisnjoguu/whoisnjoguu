import os
import praw
from dotenv import load_dotenv

load_dotenv()

# Initialize a Reddit instance with your API credentials
reddit = praw.Reddit(client_id=os.environ['client_id'],
                     client_secret=os.environ['client_secret'],
                     username=os.environ['username'],
                     password=os.environ['password'],
                     user_agent=os.environ['user_agent']
                    )

def get_top_post():
    # Define the subreddit to fetch the top post from
    subreddit = reddit.subreddit('ProgrammerHumor')

    # Get the top post from the past 24 hours
    top_post = subreddit.top(time_filter='day',limit=1)

    # Extract the relevant information from the top post
    for post in top_post:
        title = post.title
        author = post.author.name
        link = post.permalink
        score = post.score
        

    return post.url


if __name__ == '__main__':
    get_top_post()
