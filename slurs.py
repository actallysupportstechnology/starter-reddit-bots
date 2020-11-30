import praw, time, traceback

slurs = ["<slur>",
         "<slur2>",
         "<slur3>"]

mods = ["<mod>",
        "<mod2>",
        "<mod3>"]

slurwarningmessage = """
1 - **Sitewide Rule 1: NO BULLYING, HARASSMENT, or BIGOTRY**

2 - Your comment was removed because it contains a rude word

3 - If you have any questions or comments about this action, **Use this link to send us a mod mail message** [here](https://www.reddit.com/message/compose?to=%2Fr%2FRedditMoment&subject=About my removed comment&message=I'm writing to you about the following removal: {0}. %0D%0DMy issue is:). 
"""

reddit = praw.Reddit(user_agent="<user agent>",
                     client_id="<client id>",
                     client_secret="<client secret>",
                     username="<username>",
                     password="<password>")

while True:
    try:
        for submission in reddit.subreddit("<sub>").stream.comments(skip_existing=True):
            for slur in slurs:
                if slur in comment.body and comment.author.name not in mods:
                    comment.reply(slurwarningmessage.format(comment.permalink)).mod.distinguish()
                    comment.mod.remove()
                    break
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down :(')
        quit()
