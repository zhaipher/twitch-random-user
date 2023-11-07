import twitchio

# Create a new Twitch client
client = twitchio.Client()

# Connect to the Twitch chat
client.connect()

# Listen for messages
@client.event
async def on_message(message):
  # Do something with the message

# Run the client
client.run()
