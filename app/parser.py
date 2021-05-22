import datetime
from os import listdir
import json

def parse_whatsapp(filename):

    file = open(filename,"r")

    lines = file.readlines()

    formatted = []

    for line in lines:
        try:
            date = datetime.datetime.strptime(line[:17], '%d/%m/%Y, %H:%M')

            string = print(line[17:].split(":")[1].replace('\n',''))
            #print(datetime.dline[:15])
            message = {
                "content": string,
                "sender": line[17:].split(":")[0],
                "timestamp": date
            }
            formatted.append(message)
        except Exception as e:
            #print(e)
            pass
        
    return formatted


def parse_messenger():
    

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
            message = {'sender_name': message['sender_name'], 'timestamp': message['timestamp_ms'], 'content': message['content']}
        else:
            message = {'sender_name': message['sender_name'], 'timestamp': message['timestamp_ms'], 'content': 'SLIKA TODO'}
        messages[i] = message
    print(messages)

    return messages

#parse_messenger('fawf')