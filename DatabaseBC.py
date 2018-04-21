import sqlite3
from EncDec import enc, dec
import json
import time


def dict_factory(cursor, row):
    d = {}
    for idx, con in enumerate(cursor.description):
        d[con[0]] = row[idx]
    return d


class DataBaseBC:

    def create_table_transaction(self):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS buffer (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ok VARCHAR,
                                code VARCHAR,
                                data VARCHAR,
                                sign VARCHAR)''')
        db.commit()
        cursor.close()
        db.close()

    def create_table_block(self):

        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS block (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ok VARCHAR,
                                trans VARCHAR,
                                sign VARCHAR,
                                nonce VARCHAR,
                                hash VARCHAR,
                                time VARCHAR)''')
        db.commit()
        cursor.close()
        db.close()
        self.add_genesis()


    def add_genesis(self):
        if self.get_my_len() is None:
            t = str(int(time.time()))
            db = sqlite3.connect('DatabaseBC.db')
            cursor = db.cursor()
            cursor.execute('''INSERT INTO block (ok, trans, sign, nonce, hash, time) VALUES (?, ?, ?, ?, ?, ?)''',
                           ('0000',
                            ' ',
                            '0000',
                            '0',
                            ' ',
                            t))
            db.commit()
            cursor.close()
            db.close()

    def add_to_buffer(self, trans):
        ok = trans.get('ok')
        code = trans.get('code')
        data = trans.get('data')
        sign = trans.get('sign')

        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO buffer (OK, code, data, sign) VALUES (?, ?, ?, ?)''', (ok, code, data, sign,))
        db.commit()
        cursor.close()
        db.close()

    def add_block_to_blockchain(self, block):
        ok = block.get('ok')
        trans = block.get('trans')
        trans = json.dumps(trans, sort_keys=True)
        sign = block.get('sign')
        nonce = block.get('nonce')
        hash = block.get('hash')
        t = int(time.time())
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO block (ok, trans, sign, nonce, hash, time) VALUES (?, ?, ?, ?, ?, ?)''', (ok,  trans, sign, nonce, hash, t, ))
        db.commit()
        id = cursor.execute('''SELECT id FROM block WHERE hash = (?)''', (hash,))
        id = id.fetchone()
        cursor.close()
        db.close()
        return id[0]

    def drop_from_buffer(self, id_trans):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM buffer WHERE id = (?)''', id_trans)
        db.commit()
        cursor.close()
        db.close()


    def get_block_transaction(self, id_block):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''SELECT trans FROM block WHERE id = (?)''', (id_block,))
        trans = cursor.fetchone()
        cursor.close()
        db.close()
        return trans[0]


    def get_chain(self, id_block):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT trans FROM block WHERE id > (?)''', (id_block,))
        chain = cursor.fetchall()
        cursor.close()
        db.close()
        return chain

    def get_my_len(self):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''SELECT id FROM block''')
        id = cursor.fetchall()
        cursor.close()
        db.close()
        if id != []:
            return id[-1][0]
        else:
            return None

    def timestamp(self, id):
        # print(id)
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''SELECT time FROM block WHERE id = (?)''', (id, ))
        time = cursor.fetchone()
        # print(time)
        cursor.close()
        db.close()
        return time[-1][0]

    def buf_size(self):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.execute('''SELECT id FROM buffer''')
        id = cursor.fetchall()
        cursor.close()
        db.close()
        return id[-1][0]

# DataBaseBC().create_table_block()
# DataBaseBC().create_table_transaction()