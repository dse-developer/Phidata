import requests
from bs4 import BeautifulSoup

# Fetch the Hacker News homepage
response = requests.get('https://news.ycombinator.com/')
# Parse the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Function to get top stories
def get_top_stories(soup):
    # Find all story links
    story_links = soup.find_all('a', class_='storylink')
    # Get text from each link
    top_stories = [link.text for link in story_links]
    return top_stories

# Assign the top stories to a variable
top_stories = get_top_stories(soup)