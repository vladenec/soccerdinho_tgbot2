import sqlite3


class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """"Проверка, есть ли юзер в БД"""
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        """"Добавление юзера в БД"""
        self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_comp_geo(self, user_id, comp_geo):
        """"Добавляем страну-соревнование в таблицу users"""

    def add_team(self, user_id, comp_geo):
        """"Добавляем команду в таблицу users"""