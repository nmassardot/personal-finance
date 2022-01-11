import os
from flask import Flask
from fintoc import Fintoc
from dotenv import load_dotenv
from utils import get_last_month_total_response

load_dotenv()

API_KEY = os.getenv("SK_LIVE")
LINK_TOKEN = os.getenv("PERSONAL_TOKEN")

fintoc_client = Fintoc(API_KEY)
link = fintoc_client.links.get(LINK_TOKEN)
account = link.accounts.all(lazy=False)[0]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return {"message": "Get ready to manage your financial life!"}


@app.route("/movements/total/last-month", methods=["GET"])
def last_month_movements():
    account = link.accounts.all(lazy=False)[0]
    response = get_last_month_total_response(account)
    return {"message": "OK", "data": response}


if __name__ == "__main__":
    app.run(debug=True)
