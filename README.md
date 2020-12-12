# KeanuGifBot

Simple reddit bot to reply to comments with a Keanu Reeves Gif*.

You will have to edit your reddit keys into lines 4 -8 in main.py, see [here](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html).

\*Pronounced with a hard "Q"

# Reply Bot

If a user comments "!test" in /r/TechSupport420, bot will reply with "hello world". You will only need to edit your API keys into the reddit = praw.Reddit(...) part.

# Mod Count

The ```mod_count.py``` file will check a user's mod count and the amount of subreddits they mod. 

- Plug in your API credentials in the ```reddit = praw.Reddit(...)``` part
- Run the file: ```python3 main.py```
- It will ask you who's profile you'd like to check, just put in a valid reddit username and it'll do the rest
