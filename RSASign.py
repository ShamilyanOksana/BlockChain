import rsa
from base64 import b64decode, b64encode
from EncDec import enc, dec


class RSASign:
    def get_sign(self, pack, ck):

        pack = enc(pack)
        # print('for_sign', pack)
        sign = b64encode(rsa.sign(pack, ck, 'SHA-256'))
        sign = sign.decode()

        pack = dec(pack)
        pack.update({'sign': sign})
        # print(pack)

        return pack

    def verif_sign_trans(self, pack, ok):
        proc_pack = pack.copy()

        sign = proc_pack.pop('sign')
        sign = b64decode(sign)

        proc_pack = enc(proc_pack)
        # print(proc_pack)

        verif = rsa.verify(proc_pack, sign, ok)
        print('verif_trans: ', verif)
        return verif, pack

    def verif_sign_block(self, block, ok):
        # print('блок перед проверкой: ', block)
        proc_bl = block.copy()

        sign = proc_bl.pop('sign')
        sign = b64decode(sign)

        nonce = proc_bl.pop('nonce')

        hash = proc_bl.pop('hash')

        proc_bl = enc(proc_bl)
        # print('proc_bl, ', proc_bl)
        verif = rsa.verify(proc_bl, sign, ok)

        return verif, block
