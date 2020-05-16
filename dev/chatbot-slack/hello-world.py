import os
from slack import WebClient
from slack.errors import SlackApiError

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# Channel and message
my_channel = '<your chatbot channel>'
my_message = 'Hello world!'

try:
    response = slack_web_client.chat_postMessage(
        channel=my_channel,
        text=my_message)
    assert response["message"]["text"] == my_message

except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
