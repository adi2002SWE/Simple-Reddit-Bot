import praw
import time

reddit=praw.Reddit(client_id="-zAg2WCZhtbs8r-djAoL3g",
                   client_secret="ZoephnAz5rPmOanxdeRySOWKoV-qyQ",
                   user_agent="aditya@2002verma",
                   username="v2002A",
                   password="AVerma01@!")

subreddits=['SelfPromotionYouTube','VideosMP4','Youtubeviews','Videos','SubscribeToMe','YouTubePromoter']
tilte="Like , subscribe & share my this video"
link="https://www.youtube.com/watch?v=HzkJ7sYh39g"
count=0
for subreddit in subreddits:
    count+=1
    try:
        reddit.subreddit(subreddit).submit(tilte,url=link,send_replies=False)
        print("Sucessfully posted to", subreddit,"Posted to",count,"of",len(subreddit),"subreddits")
    except praw.exceptions.RedditAPIException as exception:
       for subexception in exception.items:
           if subexception.error_type=="RATELIMIT":
               wait=str(subexception).replace("RATELIMIT: ' You are doing thst too much . try again in","")
               if 'minutes' in wait:
                   wait=wait[:2]
                   wait=int(wait)
                   print(wait)
               else:
                  wait=1
               print("waiting for:",wait,"minutes") 
               time.sleep(wait*60)
               reddit.subreddit(subreddit).submit(tilte,url=link,send_replies=False)
               print("Sucessfully posted to", subreddit)





                


