from datetime import datetime

from os import listdir
import json

def parse_whatsapp(filename):

    file = open(filename,"r")

    lines = file.readlines()

    formatted = []

    for line in lines:
        try:
            date = datetime.strptime(line[:17], '%d/%m/%Y, %H:%M')

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

# also for instagram
def parse_messenger():
    path = "messages/inbox/"
    hoomans = []
    chats_dict_by_hooman = {}

    for hooman in listdir(path):
        with open(path + hooman + '/message_1.json', encoding='ASCII') as f:
            data = json.load(f)#.items())
        hoomans.append(hooman)
        chats_dict_by_hooman[hooman] = data['messages']
    
    for hooman in hoomans:
        messages = chats_dict_by_hooman[hooman]
        for i, message in enumerate(messages):
            if 'content' in message:
                new_content = message['content']    
            else:
                new_content = 'SLIKA TODO'
            
            message = {'sender_name': message['sender_name'], 'timestamp': datetime.fromtimestamp(message['timestamp_ms']/1000.0), 'content': new_content}
            messages[i] = message

        chats_dict_by_hooman[hooman] = messages

    return chats_dict_by_hooman


def group_by_day(messages):

    grouped = {}

    for message in messages:
        date = message["timestamp"].strftime('%d/%m/%y')
        if date not in grouped:
            grouped[date] = []
        
        grouped[date].append(message["content"])

    # join into single string
    for key in grouped:
        grouped[key] = ". ".join(grouped[key])
    
    return grouped    

chats_dict = parse_messenger()
messages = [(k,chats_dict[k]) for k in chats_dict][3]
grouped = group_by_day(messages[1])
print(grouped)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def count_word_frequency_in_text(text):
    # Tokenizing the text
    stopWords = set(stopwords.words("slovene"))
    stopWords = stopWords.union({'.',',',':','!','?','haha','hahah','hahaha'})
    words = word_tokenize(text)
    
    # Creating a frequency table to keep the 
    # score of each word
    
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable