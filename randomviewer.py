import random
def random_user():
    users = []
    for user in chat.users:
        users.append(user.name)
    return random.choice(users)
def response(message):
    user = random_user()
    return f": {user}"
if message.content == "!roll":
    response(message)
