import ron
from flask import Flask

website = Flask(__name__)

@website.route("/")
def index():
    quote = ron.get_quote()
    return "<html><body><p>" + quote[0] + "</p></body></html>"

@website.route("/<num>")
def index_multi(num):
    quotes = ron.get_quotes(num)
    html = "<html><body>"
    for x in quotes:
        html += "<p>" + x + "</p>"
    html += "</body></html>"
    return html
