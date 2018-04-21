import json
import rsa
import DatabaseBC
from EncDec import enc, dec
import RSASign
import rsa
import check_trans
import save_changes
import Network

class BlockChain:
    def __init__(self, package):
        package = dec(package)
        if package.get('type') == 'transaction':
            package.pop('type')
            self.proc_transaction(package)
        elif package.get('type') == 'block':
            package.pop('type')
            self.proc_block(package)


        elif package.get('type') == 'synchronize':
            package.pop('type')
            self.synchronize(package)
        elif package.get('type') == 'chain':
            package.pop('type')
            self.chain(package)


#РАБОТАЕТ (ПРИНЯЛИ ТРАНЗАКЦИЮ ИЗ СЕТИ) (ПРИНЯЛИ ТРАНЗАКЦИЮ ИЗ БАЗЫ)
    def proc_transaction(self, trans):

        ok = trans.get('ok')
        ok_e, ok_n = ok.split(' ')
        ok = rsa.PublicKey(int(ok_n), int(ok_e))

        verif = RSASign.RSASign().verif_sign_trans(trans, ok)

        if verif:
            db = DatabaseBC.DataBaseBC()
            db.add_to_buffer(trans)
        return verif

# РАБОТАЕТ (ПРИНЯЛИ ТРАНЗАКЦИЮ ИЗ БЛОКА)
    def proc_block_transaction(self, trans):
        # print('trance', trans)
        for i in range(len(trans) - 1):
            if str(type(trans)) == "<class 'str'>":
                trans = json.loads(trans)
            current_tr = trans.get(str(i + 1))
            if current_tr is not None:
                proc_tr = json.loads(current_tr)
                ok = proc_tr.get('ok')
                ok_e, ok_n = ok.split(' ')
                ok = rsa.PublicKey(int(ok_n), int(ok_e))
                # print('proc_tr: ', proc_tr)
                try:
                    verif = RSASign.RSASign().verif_sign_trans(proc_tr, ok)
                    print(' Verification TRANS OK')
                except Exception:
                    print(' Verification TRANS failed')
                    return 0
            else:
                return True

    # РАБОТАЕТ (ОБРАБОТКА БЛОКА)
    def proc_block(self, block):
        ok = block.get('ok')
        ok_e, ok_n = ok.split(' ')
        ok = rsa.PublicKey(int(ok_n), int(ok_e))
        # print('BLOCKCAIN->proc_block()', block)
        try:
            # отдает словарь / принимает словарь
            time = block.pop('time')
            verif_block, block = RSASign.RSASign().verif_sign_block(block, ok)
            print(' Verification BLOCK OK')
        except Exception:
            print(' Verification BLOCK failed')
            return 0
        else:
            block.update({'time':time})
            trans = block.get('trans')
            # print('trance:', trans)
            # print(type(trans))
            if self.proc_block_transaction(trans):
                db = DatabaseBC.DataBaseBC()
                id = db.add_block_to_blockchain(block)
                # save_changes.Changes().get_transaction_from_bd(id)

    def synchronize(self, pack):
        id = int(pack.get('chain'))
        ip = pack.get('ip')
        my_len = DatabaseBC.DataBaseBC().get_my_len()
        if my_len > id:
            chain = DatabaseBC.DataBaseBC().get_chain(id)
            chain = enc(chain)
            data = {'type': 'chain',
                    'chain': chain}
            Network.Network().send_to_user(ip, chain)

    def chain(self, pack):
        ch = enc(pack)
        print(ch)
