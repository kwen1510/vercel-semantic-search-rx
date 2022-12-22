from flask import Flask, render_template, request, jsonify
import os
import json
import requests

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
        
    return render_template('results.html', responses=responses_array, query=query)