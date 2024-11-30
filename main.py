import requests

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_updates():
    url = BASE_URL + 'getUpdates'
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = BASE_URL + 'sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response.json()

if name == 'main':
    updates = get_updates()
    print(updates)
    if updates['result']:
        last_chat_id = updates['result'][-1]['message']['chat']['id']
        send_message(last_chat_id, 'Hello from your bot!')