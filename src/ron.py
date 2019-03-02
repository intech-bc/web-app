import requests

url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

def get_quote():
    r = requests.get(url)
    return r.json()

def get_quotes(num):
    r = requests.get(url + "/" + num)
    return r.json()
