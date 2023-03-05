import requests
import pandas as pd
import datetime
import time

update_time = 5  # в секундах


#        else:
#          print('Нет изменений')

# функция получения таблицы с результатами текущих матчей
# * event['Eps'] == "NS" в случае если матч еще не начался но уже попал в таблицу

# функция для отправки текста уведомления
def get_message(df, old_df):
    for row in df.index:
        for row_old in old_df.index:
            if df[['Home', 'Away']].iloc[[row]].equals(old_df[['Home', 'Away']].iloc[[row_old]]) == True:
                if df[['Home', 'Away', 'Home_Score', 'Away_Score']].iloc[[row]].equals(
                        old_df[['Home', 'Away', 'Home_Score', 'Away_Score']].iloc[[row_old]]) == False:
                    message = str(str(df['Home_Score'][row]) + ' -- ' + str(df['Away_Score'][row]) + '  ' + str(
                        df['Home'][row]) + ' vs ' + str(df['Away'][row]) + ' (' + str(df['Match_Clock'][row]) + ')')
                    return (message)
                break


def get_live_data():
    url = "https://prod-public-api.livescore.com/v1/api/react/live/soccer/0.00?MD=1"
    jsonData = requests.get(url).json()
    rows = []
    for stage in jsonData['Stages']:
        events = stage['Events']
        for event in events:
            if event['Eps'] == "NS":
                gameDateTime = event['Esd']
                date_time_obj = datetime.datetime.strptime(str(gameDateTime), '%Y%m%d%H%M%S')
                gameTime = date_time_obj.strftime("%H:%M")

                homeTeam = event['T1'][0]['Nm']
                homeScore = 0

                copmetitionName = event['Stg']['Snm']
                copmetitionName2 = event['Stg']['Cnm']

                awayTeam = event['T2'][0]['Nm']
                awayScore = 0

                matchClock = event['Eps']

                row = {
                    'Home': homeTeam,
                    'Home_Score': homeScore,
                    'Away': awayTeam,
                    'Away_Score': awayScore,
                    'Match_Clock': matchClock,
                    'Competition': copmetitionName,
                    'Geo': copmetitionName2,
                }
                rows.append(row)
            else:
                gameDateTime = event['Esd']
                date_time_obj = datetime.datetime.strptime(str(gameDateTime), '%Y%m%d%H%M%S')
                gameTime = date_time_obj.strftime("%H:%M")

                homeTeam = event['T1'][0]['Nm']
                homeScore = event['Tr1']

                copmetitionName = event['Stg']['Snm']
                copmetitionName2 = event['Stg']['Cnm']

                awayTeam = event['T2'][0]['Nm']
                awayScore = event['Tr2']

                matchClock = event['Eps']

                row = {
                    'Home': homeTeam,
                    'Home_Score': homeScore,
                    'Away': awayTeam,
                    'Away_Score': awayScore,
                    'Match_Clock': matchClock,
                    'Competition': copmetitionName,
                    'Geo': copmetitionName2,
                }
                rows.append(row)

    live_df = pd.DataFrame(rows)
    return (live_df)


# API в одну функцию
def request_livescore(filter):  # переменная a нужна только для счетчика
    old_df = get_live_data().query('Competition in @filter').reset_index(drop=True)
    time.sleep(update_time)
    df = get_live_data().query('Competition in @filter').reset_index(drop=True)
    if len(df) != 0 and len(old_df) != 0:
        message_to_send = str(get_message(df, old_df))
        if message_to_send != 'None':
            telegram_bot_sendtext(message_to_send, users_list)
            request_livescore(filter)
        else:
            request_livescore(filter)
    else:
        # telegram_bot_sendtext('No matches', users_list)
        request_livescore(filter)


from send_message_func import telegram_bot_sendtext
from config import users_list


# API в одну функцию без фильтра по всем матчам для теста
def request_livescore_all():
    old_df = get_live_data()  ##.query('Competition in @filter').reset_index(drop=True)
    time.sleep(update_time)
    df = get_live_data()  ##.query('Competition in @filter').reset_index(drop=True)
    # print("Прошел круг", a)
    if len(df) != 0 and len(old_df) != 0:
        message_to_send = str(get_message(df, old_df))
        if message_to_send != 'None':
            telegram_bot_sendtext(message_to_send, users_list)
            request_livescore_all()
        else:
            request_livescore_all()
    else:
        telegram_bot_sendtext('No matches', users_list)
        request_livescore_all()


def request_livescore_all_new():
    old_df = get_live_data()  ##.query('Competition in @filter').reset_index(drop=True)
    time.sleep(update_time)
    df = get_live_data()  ##.query('Competition in @filter').reset_index(drop=True)
    # print("Прошел круг", a)
    if len(df) != 0 and len(old_df) != 0:
        message_to_send = str(get_message(df, old_df))
        if message_to_send != 'None':
            return (message_to_send)
    else:
        request_livescore_all_new()


def new_func():
    print(1)


request_livescore_all_new()
