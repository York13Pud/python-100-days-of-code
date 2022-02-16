from bs4 import BeautifulSoup

# To read a file, you first need to open it in Python (this will not open it in an app):
with open("./website.html") as file_to_use:
    # We then read the contents of the file as a variable. The file is auto-closed when using "with":
    contents = file_to_use.read()

# Use BS4 to parse the contents variable and make an object from it.
# Note: There are multiple parsers available but the standard one is html.parser:
soup = BeautifulSoup(contents, 'html.parser')

# Print out the full contents of "soup" in a pretty format:
print(soup.prettify())

# Print the title in the HTML file:
print(soup.title)

# Print the name of the title tag in the HTML file:
print(soup.title.name)

# Print the contents of the title tag in the HTML file:
print(soup.title.string)

# Create a list that contains all of the h3 tags in the "soup" variable:
h3_tags = (soup.find_all(name="h3"))

# Print out only the text in the h3 tags:
for h3_tag in h3_tags:
    print(h3_tag.getText())

# Create a list that contains all of the a tags in the "soup" variable:    
anchor_tags = (soup.find_all("a"))

# Print out only the url in the href tags:
for a_tag in anchor_tags:
    print(f"anc: {a_tag.get('href')}")

# Find the first h1 tag with the id of name:
# Note: you can use it to look for a class as well but you must use class_ as class is a reserved method in python.
heading = soup.find(name="h1", id="name")

# Print the full h1 tag that it finds:
print(heading)

# Print only the text in the tag. No for loop is needed as there is only on result:
print(heading.getText("id"))

# Note: Use find_all() for multiple results, which will add each one found to a list.
# Note: Use find when you only need to find something once. It is returned as a string.

# You can also use CSS selectors to find what you are looking for:
company_url = soup.select_one(selector="p a")
print(company_url)

# Use the CSS id selector that was named name:
name = soup.select_one(selector="#name")
print(f"name: {name.getText()}")

# Find all of the elements that use a CSS class (.) called heading. This adds each to a list:
all_css_headings = soup.select(".heading")
print(all_css_headings)
for css_heading in all_css_headings:
    print(css_heading.getText())