
@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    update = request.get_json()
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            send_message(chat_id, 'Welcome to the Key Generator Bot! Use /generate to start generating keys.')
        elif text == '/generate':
            send_message(chat_id, 'Generating keys...')
            # Here you would trigger the key generation process, similar to how it's done in the JavaScript code.
            # This might involve interacting with your JavaScript code via HTTP requests, depending on your setup.
        else:
            send_message(chat_id, 'Unknown command. Please use /start or /generate.')

    return 'ok', 200

def send_message(chat_id, text):
    url = TELEGRAM_API_URL + 'sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(port=5000)
