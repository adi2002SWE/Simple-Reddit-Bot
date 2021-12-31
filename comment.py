import praw
import random

reddit=praw.Reddit(client_id="-zAg2WCZhtbs8r-djAoL3g",
                   client_secret="ZoephnAz5rPmOanxdeRySOWKoV-qyQ",
                   user_agent="aditya@2002verma",
                   username="v2002A",
                   password="AVerma01@!")

list=["Education is the most powerful weapon which you can use to change the world",
      "Education is simply the soul of a society as it passes from one generation to another",
      "The whole purpose of education is to turn mirrors into windows",
      "The function of education is to teach one to think intensively and to think critically. Intelligence plus character – that is the goal of true education",
      "Education is one thing no one can take away from you."]

subreddit=reddit.subreddit("Education")
for post in subreddit.hot(limit=10):
    for comments in post.comments:
        if hasattr(comments,"body"):
            comment_lower=comments.body.lower()
            if "education" in comment_lower:
                random_index=random.randint(0,len(list)-1)
                comments.reply(list[random_index])
            
