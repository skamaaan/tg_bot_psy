from conf import bot
import sqlite3 as db


def db_connect():
    global database, cursor
    database = db.connect('db/db_menu')
    cursor = database.cursor()
    if database:
        print("DB connection OK")

    database.execute('CREATE TABLE IF NOT EXISTS {}('
                     'pic TEXT,'
                     'title TEXT,'
                     'description TEXT,'
                     'price INT,'
                     'user INT)'.format('menu'))
    database.commit()


async def db_add(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?,?,?,?,?)', tuple(data.values()))
        database.commit()


async def db_read(message):
    for part in cursor.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, part[0],
                             f'{part[1]}\nDescription: {part[2]}\nPrice: {part[3]}\nUser: {part[4]}')
