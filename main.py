from hashlib import sha256
import base64
import hmac
import os
import codecs

from flask import Flask, request

app = Flask('app')

@app.route('/webhook', methods=["POST"])
def webhook():
    # Get HMAC and calculated by Turn from request header.
    received_hmac = request.headers['X-Turn-Hook-Signature']

    # Calculate an HMAC for the request payload using secret as sourced 
    # from Turn(available in Secret column on Settings -> API & Webhooks page).
    secret = os.environ['SECRET']
    h = hmac.new(codecs.encode(secret), request.data, sha256)
    calculated_hmac = base64.b64encode(h.digest()).decode('ascii')

    print(f'Received HMAC: {received_hmac}')
    print(f'Calculated HMAC: {calculated_hmac}')

    # If received and calculated HMAC matches proceed with processing
    # webhook since it was in fact received from Turn. Otherwise abort 
    # processing.
    if received_hmac == calculated_hmac:
      # ... do some things here ...
      return "Valid HMAC received", 200
    else:
      return "Invalid HMAC received.", 403

@app.route('/')
def index():
  return 'The Turn Webhook API endpoint is at /webhook'


app.run(host='0.0.0.0', port=8080)