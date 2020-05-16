import os
from slack import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events")

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    
    # If the incoming message contains "goodbye", then respond with a "hello" message
    if message.get("subtype") is None and "goodbye" in message.get('text'):
        my_message = "Hello <@%s>! :tada:" % message["user"]
        try:
            response = slack_web_client.chat_postMessage(
                channel = message["channel"],
                text = my_message)
            assert response["message"]["text"] == my_message

        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"API Error: {e.response['error']}")

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("Error Event: " + str(err))

# Start the server on port 3000
slack_events_adapter.start(port=3000)