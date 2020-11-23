import praw, time, random, webbrowser, traceback

reddit = praw.Reddit(client_id="my client id",
                     client_secret="my client secret",
                     user_agent="my user agent",
                     username="my username",
                     password="my password")

slurwarningmessage = """
1 - **Sitewide Rule 1: NO BULLYING, HARASSMENT, or BIGOTRY**

2 - Your comment was removed because it contains a rude word

3 - If you have any questions or comments about this action, **Use this link to send us a mod mail message** [here](https://www.reddit.com/message/compose?to=%2Fr%2FRedditMoment&subject=About my removed submission&message=I'm writing to you about the following removal: {0}. %0D%0DMy issue is:). 
"""

while True:
    try:
        for comment in reddit.subreddit("<sub>").stream.comments(skip_existing=True):
            if '<slur>' or '<slur2>' in comment.body:
                comment.reply(slurwarningmessage.format(comment.permalink))
                comment.mod.remove()
                print('Replied to comment' + comment.id)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
