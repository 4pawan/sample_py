import os
import requests
from urllib.parse import urlparse

# List of URLs to save
urls = [
    'https://www.drcf.org.uk/news-and-events/news/new-article-drcf-delivering-impact-through-cooperation',
    'https://www.drcf.org.uk/about-us',
    # Add more URLs here
]

# Directory to save the HTML files
save_dir = 'saved_pages'

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i, url in enumerate(urls):
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Create a file name based on the URL or index
        parsed_url = urlparse(url)
        last_part = parsed_url.path.rstrip('/').split('/')[-1]
        file_name = f'page_{i+1}_{last_part}.html'
        file_path = os.path.join(save_dir, file_name)

        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f'Saved {url} to {file_path}')

    except requests.exceptions.RequestException as e:
        print(f'Failed to save {url}: {e}')
