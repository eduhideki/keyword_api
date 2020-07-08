# app.py
from flask import Flask, request, jsonify
import pandas as pd
from pytrends.request import TrendReq
import wikipedia
app = Flask(__name__)

def get_keywords(theme):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[theme])
    return pytrend.related_queries()[theme]['top']['query'].to_json()

@app.route('/getmsg/', methods=['GET'])
def respond():
    theme = request.args.get("theme", None)
    response={}

    # Check if user sent a name at all
    if not theme:
        response["ERROR"] = "Campo Tema vazio"
    # Now the user entered a valid name
    else:
        response = get_keywords(theme)

    # Return the response in json format
    return response

# A welcome message to test our server
@app.route('/')
def index():
    return '<a href="https://keyword-suggester.vercel.app/">API do site</h1>'

if __name__ == '__main__':
    app.run(threaded=True)