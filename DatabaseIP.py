import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, con in enumerate(cursor.description):
        d[con[0]] = row[idx]
    return d

class DataBaseIP:

    def __init__(self):
        self.create_table()

    def create_table(self):
        db = sqlite3.connect('DatabaseIP.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ip_addresses (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ip VARCHAR UNIQUE)''')
        db.commit()
        cursor.close()
        db.close()

    def add_ip(self, ip):
        db = sqlite3.connect('DatabaseIP.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO ip_addresses (ip) VALUES (?)''', (ip,))
        db.commit()
        cursor.close()
        db.close()

    def get_ip_list(self):
        db = sqlite3.connect('DatabaseIP.db')
        cursor = db.cursor()
        cursor.row_factory = dict_factory
        ip_list = cursor.execute('''SELECT ip FROM ip_addresses''')
        ip_list = ip_list.fetchall()
        db.commit()
        cursor.close()
        db.close()
        return ip_list

