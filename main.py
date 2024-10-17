import requests
import selectorlib

# input
URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/39.0.2171.95 Safari/537.36'}


def scrape(URL):
    """ scrape the page source from url"""
    response = requests.get(URL, headers=HEADERS)
    source = response.text
    return source


if __name__ == "__main__":
    print(scrape(URL))

