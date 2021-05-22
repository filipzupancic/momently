from datetime import datetime

from os import listdir
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

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


def parse_instagram():
    return parse_inbox_type("messages/instagram/inbox")

def parse_messenger():
    return parse_inbox_type("messages/facebook/inbox")


# also for instagram
def parse_inbox_type(path):

    hoomans = []
    chats = {}

    for hooman in listdir(path)[:5]:
        with open(path + hooman + '/message_1.json') as f:
            data = json.load(f)#.items())
        hoomans.append(hooman)
        chats[hooman] = data['messages']
        
    messages = chats[hoomans[3]]
    for i, message in enumerate(messages):
        #print(i)
        if 'content' in message:
            message = {'sender_name': message['sender_name'], 'timestamp': datetime.fromtimestamp(message['timestamp_ms']/1000.0), 'content': message['content']}
        else:
            message = {'sender_name': message['sender_name'], 'timestamp': datetime.fromtimestamp(message['timestamp_ms']/1000.0), 'content': 'SLIKA TODO'}
        messages[i] = message
    #print(messages)

    return messages


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

#messages = parse_messenger()
##grouped = group_by_day(messages)
#print(grouped)



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