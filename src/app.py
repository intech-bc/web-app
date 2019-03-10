import ron
import pymongo

from pymongo import MongoClient
from flask import Flask

inFile = open("connectionString.txt", "r")
client = pymongo.MongoClient(inFile.readline())
db = client.ronSwansonQuotes

website = Flask(__name__)

@website.route("/")
def index():
    quote = ron.get_quote()
    data = {'quote':quote[0]}
    db.quotes.insert_one(data)
    return "<html><body><p>" + quote[0] + "</p></body></html>"


@website.route("/<num>")
def index_multi(num):
    quotes = ron.get_quotes(num)
    html = "<html><body>"
    for x in quotes:
        html += "<p>" + x + "</p>"
    html += "</body></html>"
    return html
