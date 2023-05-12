import io
import os
import praw
from dotenv import load_dotenv

load_dotenv()

# Initialize a Reddit instance with your API credentials
reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                     client_secret=os.environ['CLIENT_SECRET'],
                     username=os.environ['USERNAME'],
                     password=os.environ['PASSWORD'],
                     user_agent=os.environ['USER_AGENT']
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
        

    # Open the post.txt file in write mode and write the formatted string to it
    with io.open('post.txt', 'w', encoding='utf8') as post_file:
        post_file.write(post.url)


if __name__ == '__main__':
    get_top_post()
