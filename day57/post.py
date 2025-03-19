import requests

class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body

def get_data() -> list:
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    return response.json()

def set_data() -> list:
    data = get_data()
    posts = []
    for post in data:
        posts.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))
    return posts