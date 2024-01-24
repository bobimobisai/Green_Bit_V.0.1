import sqlite3 as sq
db = sq.connect('tg_users.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS accounts(
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                user_link TEXT,
                user_name TEXT)"""
                )
db.commit()

async def db_user(user_id, user_name, user_link):
    user = cur.execute("SELECT 1 from accounts WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts  (user_id, user_link, user_name) VALUES(?, ?, ?)", (user_id, user_link, user_name))
    db.commit()
