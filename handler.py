import logging
import os
import json
import urllib

import azure.functions as func
from flask import Flask, request, Response
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter
from slack_sdk.signature import SignatureVerifier

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

client = WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
signature_verifier = SignatureVerifier(os.environ["SIGNING_SECRET"])

slackBody = {
    "text": "Test"
}


@app.route('/slack/interactive-endpoint', methods=['GET','POST'])
def interactive_trigger():
    print("trigger works")
    payload = json.loads(request.form["payload"])
    if payload["type"] == "interactive_message":
        # code to handle interactive messages
        # ...
    elif payload["type"] == "block_actions":
        # code to handle block actions
        # ...
    elif payload["type"] == "dialog_submission":
        # code to handle dialog submissions
        # ...
    return Response(status=200)

@app.route('/hello', methods=['POST'])
def hello():   
    print("hello works")
    client.chat_postMessage(channel='#random', 
                            text="hello world  ",
                        )
    return Response(status=200)

def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        return func.HttpResponse(json.dumps(slackBody), 200)
    elif req.method == "POST":
        return hello()

if __name__ == '__main__':
    app.run()
# import slack
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from slackeventsapi import SlackEventAdapter
# from slack_sdk.signature import SignatureVerifier
# import os
# import pandas as pd
# import numpy as np
# import json
# import urllib
# from flask import Flask, request, Response

# from pathlib import Path              #to load environment variable
# # from dotenv import load_dotenv  
# # env_path = Path('.') / '.env'
# # load_dotenv(dotenv_path = env_path)


# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGNING_SECRET'], '/slack/events', app)

# #getting slack_bot_token from our stored environment variable
# client = WebClient(token=os.environ['SLACK_TOKEN'])
# #obtains bot id
# BOT_ID = client.api_call("auth.test")['user_id'] #gives us the bot id
# signature_verifier = SignatureVerifier(os.environ["SIGNING_SECRET"])

# @app.route('/slack/interactive-endpoint', methods=['GET','POST'])
# def interactive_trigger():
#     print("trigger works")
#     payload = json.loads(request.form["payload"])
#     # do something with the payload
#     # ...
#     if payload["type"] == "interactive_message":
#         # code to handle interactive messages
#         # ...
#     elif payload["type"] == "block_actions":
#         # code to handle block actions
#         # ...
#     elif payload["type"] == "dialog_submission":
#         # code to handle dialog submissions
#         # ...
#     return Response(status=200)
     
# @app.route('/hello', methods=['POST'])
# def hello():   
#     print("hello works")
#     client.chat_postMessage(channel='#random', 
#                             text="hello world  ",
#                         )
