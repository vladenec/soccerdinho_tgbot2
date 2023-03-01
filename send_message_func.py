import requests
from config import BOT_TOKEN, users_list


def telegram_bot_sendtext(bot_message, users):
    bot_token = BOT_TOKEN
    for i in range(len(users)):
        bot_chatID = users[i]
        send_text = 'https://api.telegram.org/bot' + str(bot_token) + '/sendMessage?chat_id=' + \
                    str(bot_chatID) + '&parse_mode=Markdown&text=' + str(bot_message)

        response = requests.get(send_text)

    return response.json()

# telegram_bot_sendtext("2222", users)
