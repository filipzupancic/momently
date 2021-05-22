from datetime import datetime

from os import listdir
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def parse_whatsapp_file(filename):
    file = open(filename,"r")

    lines = file.readlines()

    formatted = []

    for line in lines:
        try:
            date = datetime.strptime(line[:17], '%d/%m/%Y, %H:%M')

            #string = print(line[17:].split(":")[1].replace('\n',''))
            #print(datetime.dline[:15])
            message = {
                "content": string,
                "sender": line[17:].split(":")[0],
                "timestamp": date
            }
            print(date)
            formatted.append(message)
        except Exception as e:
            #print(e)
            pass
        
    return formatted

def parse_all():
    print(parse_messenger())
    return parse_instagram() + parse_whatsapp() + parse_messenger()

def parse_whatsapp():
    
    path = "messages/whatsapp/"
    formatted = []
    for filename in listdir(path):
        formatted += parse_whatsapp_file(path+filename)
    
    return formatted

def parse_instagram():
    if len(listdir("messages/instagram/")) == 0:
        return []
    return parse_inbox_type("messages/instagram/inbox/")

def parse_messenger():
    path = "messages/facebook/inbox/"
    if len(listdir("messages/facebook/")) == 0:
        return []

    return parse_inbox_type(path)


# also for instagram
def parse_inbox_type(path):

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
        date = message["timestamp"].strftime('%b %d, %Y')
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
def group_by_day_list(messages):
    grouped = group_by_day(messages)
    
    elements = [ {
        "date": key,
        "content": grouped[key]
    }  for key in grouped.keys()]

    elements.sort(key=lambda x: x["date"], reverse=True)
    return elements
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