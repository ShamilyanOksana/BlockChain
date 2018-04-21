import sqlite3
import json
import rsa
from base64 import b64decode, b64encode
import data_basa
from datetime import *
import RSASign


basa = data_basa.Basa()

"""def create_trans(OK, t_type, data, sign):
    trans = {}
    trans.update({'OK' : OK})
    trans.update({'type' : t_type})
    data = json.dumps(data)
    trans.update({'data' : data})
    trans.update({'sign' : sign})"""

def proof_trans(package):
    ok = package.get('ok')
    code = int(package.get('code'))
    data = package.get('data')
    data = json.loads(data)

    # ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ В ОТКРЫТОЕ
    if code == 1:
        OKo = data.get('OKo')
        role = data.get('role')
        fio = data.get('fio')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        if fio == '':
            return False

        if basa.get_user_by_OKo(OKo) != 0:
            return False

        if not (1 < role < 4):
            return False
        basa.add_open_user(fio, role, OKo)


    # ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ В ЗАКРЫТОЕ
    elif code == 2:
        OKz = data.get('OKz')
        role = data.get('role')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        OKzs = []
        dic = basa.get_close_users()
        for d in dic:
            OKzs.append(d.get('OKz'))
        if OKz not in OKzs:
            return False

        if not (1 < role < 4):
            return False
        basa.add_close_user(role, OKz)

    #  ИЗМЕНИТЬ РОЛЬ
    elif code == 3:
        OKo = data.get('OKo')
        shift = data.get('shift')



        basa.change_role(OKo, shift)

    # НАЗНАЧИТЬ В ИК
    elif code == 4:
        OKo = data.get('OKo')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        if basa.get_IK_by_OKo(OKo) != None:
            return False

        basa.go_to_IK(OKo)

    # ИСКЛЮЧИТЬ ИЗ ИК
    elif code == 5:
        OKo = data.get('OKo')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        if basa.get_IK_by_OKo(OKo) != None:
            return False

        basa.go_out_IK()

    # НАЗНАЧИТЬ АУДИТОРОМ
    elif code == 6:
        OKo = data.get('OKo')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        if basa.get_auditor_by_OKo(OKo) != None:
            return False

        basa.to_be_auditor(OKo)

    # ОТСТАВКА АУДИТОРА
    elif code == 7:
        OKo = data.get('OKo')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        if basa.get_auditor_by_OKo(OKo) == None:
            return False

        basa.not_to_be_auditor(OKo)

    # УДАЛИТЬ ПОЛЬЗОВАТЕЛЯ
    elif code == 8:
        OKo = data.get('OKo')

        OKos = []
        dic = basa.get_admins()
        for d in dic:
            OKos.append(d.get('OKo'))
        if ok not in OKos:
            return False

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        basa.delete_user(OKo)


    # СОЗДАТЬ ОТКРЫТОЕ ГОЛОСОВАНИЕ
    elif code == 10:
        OKo = data.get('OKo')
        day = data.get('day')
        month = data.get('month')
        year = data.get('year')
        during = data.get('during')
        start = datetime(year, day, month)
        finish = timedelta(days = during)

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        if during <= 0 and during > 4:
            return False

        if datetime.now() > start:
            return False

        basa.create_open_voting(ok, OKo, day, month, year, during)


    # СОЗДАТЬ ЗАКРТОЕ ГОЛОСОВАНИЕ
    elif code == 11:
        OKo = data.get('OKo')
        role = data.get('role')
        day = data.get('day')
        month = data.get('month')
        year = data.get('year')
        during = data.get('during')
        question = data.get('question')
        start = datetime(year, day, month)
        finish = timedelta(days=during)

        if basa.get_user_by_OKo(OKo) == 0:
            return False

        if during <= 0 and during > 4:
            return False

        if datetime.now() > start:
            return False

        basa.create_close_voting(role, question, day, month, year, during)

    # ПРОГОЛОСОВАТЬ ОТКРЫТО
    # elif code == 12:
    #     time = datetime.now()
    #     OKo = data.get('OKo')
    #     start = basa.get_time_from_open_vouting()



    # # ПРОГОЛОСОВАТЬ ЗАКРЫТО
    # elif code == 13:
    #
    # # ПОДСЧИТАТЬ ОТКРЫТЫЕ ГОЛОСА
    # elif code == 14:
    #
    # # ПОДСЧИТАТЬ ЗАКРЫТЫЕ ГОЛОСА
    # elif code == 15:
