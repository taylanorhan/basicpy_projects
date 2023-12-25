import requests
from bs4 import BeautifulSoup
#scraper belirli bir web sitesinde bulunan verileri toplamak için web sayfalarının htmlini analiz eder

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')  # Replace with the  HTML element in the data

        for article in articles:
            title = article.find('h2').text  # Replace with the specific tag in title
            print(f"Title: {title}")
    else:
        print("Failed to fetch the webpage.")


target_url = 'https://example.com'  # Replace with the URL of the website 
scrape_website(target_url)
