from dotenv import load_dotenv
import time
from Vidhukantwebhelper import get_blog_titles
from sendmail import sendmail



# Load the .env file
load_dotenv()

def get_added_posts(new, old):
    added_posts = []
    for x in new:
        if x not in old:
            added_posts.append(x)
    return added_posts

def get_deleted_posts(new,old):
    deleted_posts = []
    for x in old:
        if x not in new:
            deleted_posts.append(x)
    return deleted_posts


old_titles = get_blog_titles()
while True:
    time.sleep(20)
    new_titles = get_blog_titles()
    print("Got new Titles")
    if old_titles != new_titles:
        added = get_added_posts(new_titles, old_titles)
        deleted = get_deleted_posts(new_titles,old_titles)
        msg = "VidhuKant.com has updated"
        if len(added) > 0:
            msg += "\nThe Following Post(s) were added:\n" + "\n".join(added)
        if len(deleted) > 0:
            msg += "\nThe Following Post(s) were deleted:\n" + "\n".join(deleted)
        print("Sending Mail")
        sendmail(msg)
    old_titles = new_titles
