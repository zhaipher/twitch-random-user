import twitchio

client = twitchio.Client()

@client.event("message")
async def on_message(message):
    if message.content == "!roll":
        users = await client.get_users(limit=1)
        user = users[0]
        await client.send_message(message.channel, f"สุ่มผู้โชคดี: {user.name}")

client.run()
