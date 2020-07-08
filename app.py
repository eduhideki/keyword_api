# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
from pytrends.request import TrendReq
import wikipedia
app = Flask(__name__)
CORS(app)

def get_keywords(theme):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[theme])
    return pytrend.related_queries()[theme]['top']['query'].values.tolist()

@app.route('/getmsg/', methods=['GET'])
def respond():
    theme = request.args.get("theme", None)
    response={}
   
    if not theme:
        response["ERROR"] = "Campo Tema vazio"

    else:
        response["RESULTS"] = get_keywords(theme)

    return response

# A welcome message to test our server
@app.route('/')
def index():
    return '<a href="https://keyword-suggester.vercel.app/">API do site</h1>'

if __name__ == '__main__':
    app.run(threaded=True)