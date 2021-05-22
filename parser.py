from os import listdir
import json

path = "messages/inbox/"

hoomans = []
chats = {}

for hooman in listdir(path)[:2]:
    with open(path + hooman + '/message_1.json') as f:
        data = json.load(f)#.items())
    hoomans.append(hooman)
    chats[hooman] = data['messages']
    
messages = chats[hoomans[1]]
for i, message in enumerate(messages):
    print(i)
    if 'content' in message:
        message = {'sender_name': message['sender_name'], 'timestamp_ms': message['timestamp_ms'], 'content': message['content']}
    else:
        message = {'sender_name': message['sender_name'], 'timestamp_ms': message['timestamp_ms'], 'content': 'SLIKA TODO'}
    messages[i] = message
print(messages)

