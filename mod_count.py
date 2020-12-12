import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

usr = input("What user should we look at? ")
sub_count = 0
mod_count = 0

for subreddit in reddit.redditor(usr).moderated():
    sub_count += subreddit.subscribers
    mod_count += 1
    
print("/u/{} mods {} subreddits total and has a total of {} subscribers.".format(usr,mod_count,sub_count))
