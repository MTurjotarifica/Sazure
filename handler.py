import logging
import os
import json
import requests

import azure.functions as func
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.signature import SignatureVerifier

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Verify the Slack request signature
    signature_verifier = SignatureVerifier(os.environ["SLACK_SIGNING_SECRET"])
    try:
        signature_verifier.validate(
            req.headers.get("X-Slack-Request-Timestamp"),
            req.headers.get("X-Slack-Signature"),
            req.get_body()
        )
    except Exception as e:
        return func.HttpResponse("Signature verification failed", status_code=400)

    # Parse the request body
    request_body = req.get_json()
    command = request_body["command"]
    text = request_body["text"]

    # Handle the command
    if command == "/hello":
        # Your code to handle the command goes here
        # ...
        response = {
            "response_type": "in_channel",
            "text": "Your command was processed successfully!"
        }
        return func.HttpResponse(json.dumps(response), mimetype="application/json")

    return func.HttpResponse("Unknown command", status_code=200)





# import logging
# import json
# import azure.functions as func
# from flask import Flask, request

# import requests

# response = requests.get("https://sazurebotapp.azurewebsites.net/hello")
# if response.status_code == 200:
#     print("The endpoint is accessible")
# else:
#     print("The endpoint is not accessible")

# app = Flask(__name__)

# @app.route('/hello', methods=['POST'])
# def hello():
#     # Your code to handle the request
#     # ...
#     return "Hello World", 200

# @func.HttpTrigger
# def main(req: func.HttpRequest) -> func.HttpResponse:
#     request_body = req.get_json()
#     # Your code to handle the request
#     # ...
#     return func.HttpResponse(json.dumps({"message": "Hello World"}), 200)


# import logging
# import os
# import json
# import urllib
# import requests

# import azure.functions as func
# from flask import Flask, request, Response
# from slack_sdk import WebClient
# from slackeventsapi import SlackEventAdapter
# from slack_sdk.signature import SignatureVerifier

# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGNING_SECRET'], '/slack/events', app)

# client = WebClient(token=os.environ['SLACK_TOKEN'])
# BOT_ID = client.api_call("auth.test")['user_id']
# signature_verifier = SignatureVerifier(os.environ["SIGNING_SECRET"])

# slackBody = {
#     "text": "Test"
# }


# @app.route('/slack/interactive-endpoint', methods=['GET','POST'])
# def interactive_trigger():
#     print("trigger works")
#     payload = json.loads(request.form["payload"])
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
#     return Response(status=200)

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     data = {"text": "Test"}
#     response = requests.post("https://makinazure.azurewebsites.net/api/makin?code=nCcniIWN7zHY-f4c17VonoQaXMguPPKBy8P2BdFJkrbvAzFubIp7sg==", json=data)
#     return func.HttpResponse(json.dumps(response.json()), 200)

# if __name__ == '__main__':
#     app.run()
    
    
    
    
    
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
