from flask import Flask, render_template
from api.financial_data import EODHDAPIsDataFetcher
from config import API_TOKEN

app = Flask(__name__)

data_fetcher = EODHDAPIsDataFetcher(API_TOKEN)


@app.route("/")
def index():
    exchanges = data_fetcher.fetch_exchanges()
    return render_template("exchanges.html", exchanges=exchanges)


if __name__ == "__main__":
    app.run(debug=True)
