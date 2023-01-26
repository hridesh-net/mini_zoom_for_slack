import requests
from slack_bolt import App
import datetime
import os
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
from slack_sdk.web import WebClient
from slack_sdk.errors import SlackApiError
from onboarding_tutorial import OnboardingTutorial

slack_app_token = 'xapp-1-A04JPDE8TB6-4630184488693-b28f67863d3a9843115299cdafc3454af88c81261bd17544a075eef3fe8954b6'
# Initializes your app with your bot token and socket mode handler
app = App(token='xoxb-4517185332675-4618494576215-IC7Y0fyKvOW3ZjKc36m7KP5v')

onboarding_tutorials_sent = {}


def start_onboarding(user_id: str, channel: str, client: WebClient):
    # Create a new onboarding tutorial.
    onboarding_tutorial = OnboardingTutorial(channel)

    # Get the onboarding message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the onboarding message in Slack
    response = client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a user
    # has completed an onboarding task.
    onboarding_tutorial.timestamp = response["ts"]

    # Store the message sent in onboarding_tutorials_sent
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = onboarding_tutorial


def log_request(logger, body, next):
    logger.debug(body)
    next()


@app.message("hello mini zoom")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn",
                         "text": f"Hey there <@{message['user']}> Please Authorize your zoom account!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Authenticate"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}> click to Authorize!"
    )


@app.action("button_click")
def action_button_click(body, ack, say, client, logger):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> ")
    logger.info(body)
    ack()
    # print(respond)


# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.

# Note: Bolt provides a WebClient instance as an argument to the listener function
# we've defined here, which we then use to access Slack Web API methods like conversations_open.
# For more info, checkout: https://slack.dev/bolt-python/concepts#message-listening
@app.event("team_join")
def onboarding_message(event, client):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    # Get the id of the Slack user associated with the incoming event
    user_id = event.get("user", {}).get("id")

    # Open a DM with the new user.
    response = client.conversations_open(users=user_id)
    channel = response["channel"]["id"]

    # Post the onboarding message.
    start_onboarding(user_id, channel, client)


# ============= Reaction Added Events ============= #
# When a users adds an emoji reaction to the onboarding message,
# the type of the event will be 'reaction_added'.
# Here we'll link the update_emoji callback to the 'reaction_added' event.
@app.event("reaction_added")
def update_emoji(event, client):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    # Get the ids of the Slack user and channel associated with the incoming event
    channel_id = event.get("item", {}).get("channel")
    user_id = event.get("user")

    if channel_id not in onboarding_tutorials_sent:
        return

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    # Mark the reaction task as completed.
    onboarding_tutorial.reaction_task_completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = client.chat_update(**message)


# =============== Pin Added Events ================ #
# When a users pins a message the type of the event will be 'pin_added'.
# Here we'll link the update_pin callback to the 'pin_added' event.
@app.event("pin_added")
def update_pin(event, client):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    # Get the ids of the Slack user and channel associated with the incoming event
    channel_id = event.get("channel_id")
    user_id = event.get("user")

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    # Mark the pin task as completed.
    onboarding_tutorial.pin_task_completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = client.chat_update(**message)


# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@app.event("message")
def message(event, client):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if text and text.lower() == "start":
        return start_onboarding(user_id, channel_id, client)


logger = logging.getLogger(__name__)
client = WebClient(token='xoxb-4517185332675-4618494576215-IC7Y0fyKvOW3ZjKc36m7KP5v')
# Create a timestamp for tomorrow at 9AM
tomorrow = datetime.date.today() + datetime.timedelta(days=0)
scheduled_time = datetime.time(hour=18, minute=35)
schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time)
sec = schedule_timestamp.timestamp()

# Channel you want to post message to
channel_id = "C04FX01441E"

try:
    # Call the chat.scheduleMessage method using the WebClient
    result = client.chat_scheduleMessage(
        channel=channel_id,
        text="Looking towards the future",
        post_at=sec
    )
    # Log the result
    logger.info(result)

except SlackApiError as e:
    logger.error("Error scheduling message: {}".format(e))

# Start your app
if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    SocketModeHandler(app, slack_app_token).start()
