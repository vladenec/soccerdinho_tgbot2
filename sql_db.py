import sqlite3


class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_users(self, status=True):
        """ Получаем всех активных подписчиков"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users' WHERE status = ?", (status,)).fetchall()

    def user_exists(self, user_id):
        """"Проверка, есть ли юзер в БД"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, status=True):
        """"Добавление юзера в БД"""
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' ('user_id','status') VALUES (?,?)", (user_id, status))
            return self.connection.commit()

    def update_subcription(self, user_id, status):
        """ Обновить статус подписки"""
        return self.cursor.execute("UPDATE 'users' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))

    def close(self):
        """Закрываем соединения с БД"""
        self.connection.close()


""" В СЛЕДУЮЩУЮ ВЕРСИЮ """


def add_comp_geo(self, user_id, comp_geo):
    """"Добавляем страну-соревнование в таблицу users"""


def add_team(self, user_id, comp_geo):
    """"Добавляем команду в таблицу users"""
