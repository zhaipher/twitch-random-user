import twitchio

client = twitchio.Client(
    client_id="8kdh03pq2h0cs41lz6l85pqizwwzeu",
    client_secret="ikulw4d1fisgwn8af9e1uyrzgcp78l",
    access_token="xdlrxcdi4gsre3px67uc4pyu4hgvo7"
)

@client.event("message")
async def on_message(message):
    if message.content == "!roll":
        users = await client.get_users(limit=1)
        user = users[0]
        await client.send_message(message.channel, f": {user.name}")
client.run()
