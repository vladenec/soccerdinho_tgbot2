import sqlite3

try:
    conn = sqlite3.connect("notify_livescore.db")
    cursor = conn.cursor()

    # создаем пользователя
    cursor.execute("INSERT OR IGNORE INTO 'users' (user_id) VALUES (?)", (313,))
    # подтверждаем изменения
    conn.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if (conn):
        conn.close()
