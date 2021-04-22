from flask import Flask
import os
import requests

app = Flask('app')

TOKEN = os.environ.get("TOKEN")

@app.route('/')
def index():
  return 'The Turn Webhook API endpoint is at /webhook'

@app.route('/webhook', methods=["POST"])
def webhook():
    from flask import request
    json = request.json
    return ""


app.run(host='0.0.0.0', port=8080)