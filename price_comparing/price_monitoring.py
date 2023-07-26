#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


TOKENS = {
    "BTC": "https://www.google.com/finance/quote/BTC-USD?hl=ru&gl=RU",
    "ETH": "https://www.google.com/finance/quote/ETH-USD?hl=ru&gl=RU}",
    "ADA": "https://www.google.com/finance/quote/ADA-USD?hl=ru&gl=RU",
}


def display_price(user_agent, token_name):
    """
    The function display the last actual price via Google Finance
    :param user_agent: the current user agent
    :param token_name: a variable that contains an exchange url page from Google Finance
    :return: the last actual price
    """
    # create a header for accessing  our URL page
    headers = {"user_agent": user_agent}

    # request that URL page and put it in html object
    html = requests.get(token_name, headers)

    soup = BeautifulSoup(html.content, "html.parser")
    price = soup.findAll("div", {"class": "YMlKec fxKbKc"})

    return price[0].text


def main():
    my_user_agent = "Your user agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
    for key, value in TOKENS.items():
        print(f"{key} - ${display_price(my_user_agent, value)}")


if __name__ == "__main__":
    main()
