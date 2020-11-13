import praw, time, random, webbrowser, traceback #packages for bot

#API Credentials to access reddit
reddit = praw.Reddit(client_id="my client id",
                     client_secret="my client secret",
                     user_agent="my user agent",
                     username="my username",
                     password="my password")

#list of gifs for bot to pick from, (sauce: https://imgur.com/gallery/7FXga)
gifs = ["https://i.imgur.com/LwrxCtg.gif",
        "https://i.imgur.com/2RxgOUR.mp4",
        "https://i.imgur.com/Nf0FTru.gif",
        "https://i.imgur.com/DZ8h4fs.gif",
        "https://i.imgur.com/QGHqXjg.gif"]


while True: #while loop, keeps bot running
    try: #try the following code
        for comment in reddit.subreddit("redditmoment").stream.comments(skip_existing=True): #for loop, get new comments in redditmoment, skip existing comments
            if '!KR-GIF' in comment.body: #check if a trigger is in the body of the comment
                comment.reply(random.choice(gifs)) #reply to comment with random gif
                print('Replied to comment' + comment.id) #print comment id that was replied to
    except Exception: #if any errors show up, what should we do?
        print(traceback.format_exc()) #prints error, most likely reddit went down for a bit :(
        time.sleep(60) #sleep for 60 seconds, start over
    except KeyboardInterrupt: #if user quits program, what should happen?
        print("That wasn't very wholesome of you!")
        webbrowser.open('https://i.imgur.com/RRSA8YI.mp4') #open Keanu Reeves gif in browser
        quit() #quit program
