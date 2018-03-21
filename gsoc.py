from flask import Flask
import flask
import requests
import json
app = Flask(__name__)


@app.route('/')
def hello():
    data = []
    for i in range(1,6):
        r = requests.get("https://summerofcode.withgoogle.com/api/program/current/organization/?page="+str(i)+"&page_size=48").json()
        for j in r["results"]:
            orgData = {
                'organization' : j['name'],
                'link' : j['website_url'],
                'description' : j['description'],
                'technologies' : j['technology_tags'],
                'contact': j['contact_email']

            }
            data.append(orgData)
    return flask.jsonify(result=data)

if __name__ == '__main__':
    app.run()