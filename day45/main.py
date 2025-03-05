from bs4 import BeautifulSoup
import requests


try:
    with open("saves", "r") as file:
        response = file.read()
    if not response:
        raise FileNotFoundError
except FileNotFoundError:
    response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
    with open("saves", "w") as file:
        file.write(response.text)

soup = BeautifulSoup(response, "html.parser")

titles = soup.select("span.content_content__i0P3p > h2 > strong")
for title in titles:
    print(title.text)























# soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
# print(soup.a)
# print(soup.title.string)
# print(soup.title.name)

# all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)

# for anchor in all_anchor_tags:
#     print(anchor.get_text())

# h3_class_heading = soup.find_all(name="h3", class_="heading")
# print(h3_class_heading)

# anchor = soup.find(name="a", href="https://angelabauer.github.io/cv/hobbies.html")
# print(anchor.get("href"))

# print(soup.find_all(name="p"))

# anchors = soup.select_one(selector="p a")
# print(anchors.get_text())

# lists = soup.select(selector="ul li")
# print(lists)

# headings = soup.select(selector="h3", class_="heading")
# print(headings)

# print(soup.find_all(name="li"))






