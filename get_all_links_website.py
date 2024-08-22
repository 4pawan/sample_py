import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import openpyxl
import time

# Function to fetch and parse URLs
def fetch_urls(url, visited):
    try:
        # Send GET request
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links on the page
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            full_url = urljoin(url, href)
            
            # Filter only internal links
            if urlparse(full_url).netloc == urlparse(url).netloc:
                if full_url not in visited:
                    visited.add(full_url)
                    urls.append(full_url)
                    print(f"Found URL: {full_url}")
                    
                    # Recursively fetch URLs from the linked page
                    fetch_urls(full_url, visited)
                    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

# Function to save URLs to Excel
def save_to_excel(urls, filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "URLs"
    
    # Add header
    sheet.append(["URL"])
    
    # Add URLs
    for url in urls:
        sheet.append([url])
    
    # Save the workbook
    workbook.save(filename)
    print(f"URLs saved to {filename}")

# Main function
if __name__ == "__main__":
    start_url = 'https://www.test.com/'  # Replace with the starting URL
    visited = set()  # Set to track visited URLs
    urls = []  # List to store found URLs
    
    # Start fetching URLs recursively
    fetch_urls(start_url, visited)
    
    # Save the URLs to an Excel file
    save_to_excel(urls, 'urls.xlsx')
