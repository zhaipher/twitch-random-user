import twitchio

client = twitchio.Client(
    access_token="gp762nuuoqcoxypju8c569th9wz7q5"
)
@client.event("message")
async def on_message(message):
    if message.content == "!roll":
        users = await client.get_users(limit=1)
        user = users[0]
        await client.send_message(message.channel, f": {user.name}")
client.run()
