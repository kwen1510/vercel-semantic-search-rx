from flask import Flask, render_template, request, jsonify
import os
import json
import requests
# from gspread_pandas import Spread, Client
# from google.oauth2 import service_account
# from oauth2client.service_account import ServiceAccountCredentials
# from dotenv import load_dotenv

### Load items to update Google Sheets ### 

# load_dotenv()  # take environment variables from .env.

# json_credentials = json.loads(os.getenv("credentials"))

# # Create a Google Authentication connection object
# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']

# credentials = ServiceAccountCredentials.from_json_keyfile_dict(
#                 json_credentials, scopes = scope)
# client = Client(scope=scope,creds=credentials)
# spreadsheetname = "Semantic Search Tool Responses"
# spread = Spread(spreadsheetname,client = client) 

# sh = client.open(spreadsheetname)

# # Get sheet 1
# sheet_1 = sh.sheet1

### Flask Code ###

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/results', methods=["POST"])
def testpost():

    responses_array = []

    query = request.form['search']

    url = 'https://8dshc4.deta.dev/query/'
    myobj = {'query_string': query,
            "num_responses": 5}

    x = requests.post(url, json = myobj)

    json_data = json.loads(x.text)

    for key in json_data:
        array_content = json_data[key]
        responses_array.append(array_content)

    # sheet_1.append_row(responeses_array)
        
    return render_template('results.html', responses=responses_array, query=query)