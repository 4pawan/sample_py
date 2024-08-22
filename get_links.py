import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import re

def get_all_links_recursive(url, domain, visited=None):
    if visited is None:
        visited = set()

    if url in visited:
        return visited

    visited.add(url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            abs_url = urljoin(domain, href)
            if abs_url.startswith(domain) and abs_url not in visited:
                visited = get_all_links_recursive(abs_url, domain, visited)

    return visited

def is_wrong_url(url):
    if re.search(r"[^\x00-\x7F]|_|[A-Z]", url):
        return True
    return False

def main():
    domain = input("Enter the domain URL: ")

    all_links = get_all_links_recursive(domain, domain)

    all_urls = []
    wrong_urls = []

    for link in all_links:
        if is_wrong_url(link):
            wrong_urls.append(link)
        else:
            all_urls.append(link)

    with open("all_urls.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URL"])
        for url in all_urls:
            writer.writerow([url])

    with open("wrong_urls.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Wrong URL"])
        for url in wrong_urls:
            writer.writerow([url])

    print("CSV files created: all_urls.csv, wrong_urls.csv")

if __name__ == "__main__":
    main()
