import requests
from bs4 import BeautifulSoup

def main():
    btc = 'https://www.google.com/finance/quote/BTC-USD?hl=ru&gl=RU'
    user_agent = 'Your user agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'

    headers = {'user agent': user_agent}

    html = requests.get(btc, headers)
    print(html.content)
    soup = BeautifulSoup(html.content, 'html.parser')
    # price = soup.findAll('div', {'class': 'AHmHk'})
    price = soup.findAll('Trehwb3kLMOAQooHZBaw/Q')
    print(price)


if __name__ == '__main__':
    main()
