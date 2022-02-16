from bs4 import BeautifulSoup
import requests

# Define a variable for the site to use:
site_to_use = "https://news.ycombinator.com/news"

# Open the site and assign it to a variable:
site_response = requests.get(site_to_use)
yc_web_page = site_response.text

# Parse the page using BeautifulSoupL:
soup = BeautifulSoup(yc_web_page, "html.parser")

#print(soup)

articles = soup.find_all(name = "a", class_ = "titlelink")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_ = "score")]

article_texts = []
article_links = []
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_ = "score")]

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    
    link = article_tag.get('href')
    article_links.append(link)

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# counter = 0 
# try:
#     for article in article_texts:
#         print(counter)
#         print(f"Title: {article}")
#         print(f"URL: {article_links[counter]}")
#         print(f"Upvotes: {article_upvotes[counter]}")
#         counter += 1

# except IndexError:
#     print("\nThat is all the items")

highest_upvotes = max(article_upvotes)

print("\nArticle with the most upvotes\n==============================\n")
print(f"Title: {article_texts[article_upvotes.index(highest_upvotes)]}")
print(f"Link: {article_links[article_upvotes.index(highest_upvotes)]}")
print(f"Upvotes: {highest_upvotes}")
