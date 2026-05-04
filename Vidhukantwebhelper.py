import requests
from bs4 import BeautifulSoup

def get_blog_titles():
    try:
        url = "https://scrape.vidhukant.com/blog/"

        # Get the webpage
        response = requests.get(url)

        #BeautifulSoup to read the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the list (ol tag) that contains the blog posts
        post_list = soup.find("ol", {"id": "index"}).find_all("li")

        posts = []
        for post in post_list:
            title_tag = post.find("a")
            if title_tag:
                posts.append(title_tag.text.strip())

        return posts
    except Exception as e:
        print("An error occurred while scraping:", e)
