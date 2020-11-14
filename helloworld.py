import praw, time, traceback #packages for bot

#API Credentials to access reddit
reddit = praw.Reddit(client_id="my client id",
                     client_secret="my client secret",
                     user_agent="my user agent",
                     username="my username",
                     password="my password")

while True: #while loop, keeps bot running
    try: #try the following code
        for comment in reddit.subreddit("TechSupport420").stream.comments(skip_existing=True):
            if '!test' in comment.body: #check if a trigger is in the body of the comment
                comment.reply('hello world') #reply to comment
                print('Replied to comment' + comment.id) #print comment id that was replied to
    except Exception: #if any errors show up, what should we do?
        print(traceback.format_exc()) #prints error, most likely reddit went down for a bit :(
        time.sleep(60) #sleep for 60 seconds, start over
    except KeyboardInterrupt: #if user quits program, what should happen?
        quit() #quit program
