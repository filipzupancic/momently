# momently
An application that automatically generates a digital diary based on information collected from different social apps and platforms. 



# Requirements

```
pip install -r requirements.txt

```

# Running

```
python manage.py runserver

```

# Importing data

App uses all data resources at once. Importing is described below.

## Facebook and Instagram

Download user messages from 
https://www.facebook.com/dyi?referrer=yfi_settings  |  https://www.instagram.com/download/request/. Select json format and message export only.

Unzip folder and copy contents from messages folder into messages/facebook (or instagram).

## Whatsapp 

Download chat history from whatsapp. File should be txt format. Copy file to messages/whatsapp


# Demo Frontend site

Useful link for deploying Vue

```
npm run build
```
copy dist to:

https://app.netlify.com/drop


Demo site:

Currentrly available on:

https://elastic-meitner-8b7a1d.netlify.app/
