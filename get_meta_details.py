import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://test/news-and-events/news/"

# Fetch the content of the URL
response = requests.get(url)
response.raise_for_status()  # Ensure we notice bad responses

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

meta_tag = soup.find('meta', attrs={'name': 'test.title'})

# Extract the content of the meta tag if it exists
if meta_tag:
    title_content = meta_tag.get('content', 'No content attribute found')
    print(f'Title content: {title_content}')
else:
    print('Meta tag with name "test.title" not found.')
