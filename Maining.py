import sqlite3
import Network
import rsa
import hashlib
from base64 import b64decode, b64encode
import json
from EncDec import enc, dec
import RSASign
import time
import DatabaseBC


def dict_factory(cursor, row):
    d = {}
    for idx, con in enumerate(cursor.description):
        d[con[0]] = row[idx]
    return d


class Maining:

    def block_size(self):
        while True:
            id = DatabaseBC.DataBaseBC().get_my_len()
            timestamp = int(DatabaseBC.DataBaseBC().timestamp(id))
            now = int(time.time())
            delta = now - timestamp
            if delta > (20):
                self.collecting_block(2)

    def collecting_block(self, block_size):
        block = {}
        ok, ck = rsa.newkeys(512)
        _ok = str(ok.e) + ' ' + str(ok.n)

        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.row_factory = dict_factory
        id = cursor.execute('''SELECT id FROM buffer''')
        id = id.fetchone()
        if id is None:
            pass
        else:
            id = id.get('id')
            trans = {}
            print('size:', block_size)
            for i in range(block_size):
                trans_for_block = cursor.execute('''SELECT ok, code, data, sign FROM buffer WHERE id = (?)''', (id+i,))
                trans_for_block = trans_for_block.fetchone()
                if trans_for_block is None:
                    break
                else:
                    ok_tr = trans_for_block.get('ok')
                    ok_e, ok_n = ok_tr.split(' ')
                    ok_tr = rsa.PublicKey(int(ok_n), int(ok_e))

                    try:
                        print('trans_for_block', trans_for_block)
                        RSASign.RSASign().verif_sign_trans(trans_for_block, ok_tr)
                    except:
                        print('MAINING: TRANS VERIF -- FAIL')
                    trans_for_block = json.dumps(trans_for_block, sort_keys=True)
                    trans.update({(i+1): trans_for_block})
            block.update({'trans': json.dumps(trans, sort_keys=True)})

            db.commit()
            cursor.close()
            db.close()

            block.update({'ok': _ok})
            # print('блок до подписи', block)
            # подписали блок
            # берет словарь / возвращает словарь
            block = RSASign.RSASign().get_sign(block, ck)

            block.update({'type': "block"})
            block = self.count_nonce(block)
            print('MAINING BLOCK:', block)
            self.send_block(block)
            self.delete_proof_transacton(block_size, id)

    def count_nonce(self, block):
        db = sqlite3.connect('DatabaseBC.db')
        cursor = db.cursor()
        cursor.row_factory = dict_factory
        id = cursor.execute('''SELECT id FROM block''')
        id = id.fetchall()
        id = id[-1]
        id = int(id.get('id'))
        # print(type(id))
        cursor.execute('''SELECT hash FROM block WHERE id = (?)''', (id,))
        pre_hash = cursor.fetchone()
        pre_hash = pre_hash.get('hash')
        nonce = 0
        hash_block = json.dumps(block)
        hash_block = hash_block + pre_hash
        hash_block = hash_block.encode()

        while True:

            hash = hashlib.sha256(hash_block).hexdigest()

            if hash[-4:] == '0000':
                # block = dec(block)
                block.update({'hash': hash})
                break
            else:
                nonce += 1
                # block = dec(block)
                block.update({'nonce': nonce})
                hash_block = json.dumps(block)
                hash_block = hash_block + pre_hash
                hash_block = hash_block.encode()
        print(nonce, ':', hash)
        return  block

    def send_block(self, block):
        block.update({'time': time.time()})
        net = Network.Network()
        block = enc(block)
        net.send_message(block)

    def delete_proof_transacton(self, block_size, id):
        for i in range(block_size):
            db = sqlite3.connect('DatabaseBC.db')
            cursor = db.cursor()
            cursor.execute('''DELETE FROM buffer WHERE id = (?)''', ((id+i),))
            db.commit()
            cursor.close()
            db.close()
