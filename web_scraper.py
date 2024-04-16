import requests
from bs4 import BeautifulSoup

def fetch_web_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def extract_titles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = [title.get_text() for title in soup.find_all('h1')]
    return titles

if __name__ == "__main__":
    url = "http://example.com"  # Replace with a real URL for actual use
    html_content = fetch_web_page(url)
    if html_content:
        titles = extract_titles(html_content)
        print("Titles found on the page:")
        for title in titles:
            print(title)
