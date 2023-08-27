from flask import Flask, jsonify
from fetch_price import get_crypto_prices

app = Flask(__name__)

@app.route("/crypto-prices", methods=["GET"])
def crypto_prices():
    prices = get_crypto_prices()
    return jsonify(prices)

if __name__ == "__main__":
    app.run(debug=True)