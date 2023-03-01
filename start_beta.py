from api_livescore import request_livescore_all
from api_livescore import request_livescore

# лист для фильтрации по списку соревнований
competition_list = ['Premier League', 'LaLiga Santander', 'Bundesliga', 'Ligue 1']
competition_list_1502 = ['Premier League', 'LaLiga Santander', 'Champions League', 'Round of 16', 'Bundesliga']

# Запуск функции
# request_livescore(competition_list_1502)
request_livescore_all()
