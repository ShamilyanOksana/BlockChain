import permanent
import sqlite3
import json
from datetime import  *

def dict_factory(cursor, row):
    d = {}
    for i, con in enumerate(cursor.description):
        d[con[0]] = row[i]
    return d

class Basa:

    def __init__(self):
        self.create_tables()
        self.create_roles()
        self.add_admin('SVD', '2604')
        self.add_admin('SOP', '1005')
        self.add_admin('UKS', '1111')
        self.add_admin('MDF', '7777')

    def create_tables(self):
        # ФУНКЦИЯ СОЗДАНИЯ ДАЗЫ ДАННЫХ
        self.create_table_roles()
        self.create_table_IK()
        self.create_table_open_account()
        self.create_table_open_voting()
        self.create_table_open_voting_decision()
        self.create_table_close_account()
        self.create_table_close_voting()
        self.create_table_close_voting_decision()
        return  True

    def create_table_roles(self):
        # ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦЫ РОЛЕЙ В СИСТЕМЕ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_roles)
        cursor.close()
        conn.close()
        return True

    def create_table_IK(self):
        # ФУНКЦИЯ СОЗДАНИЯ РОЛЕЙ ЧЛЕНСТВА В ИЗБИРАТЕЛЬНОЙ КОМИССИИ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        #cursor.row_factory = dict_factory
        cursor.execute(permanent.create_table_IK)
        cursor.close()
        conn.close()
        return True

    def create_table_open_account(self):
        # ФУНКЦИЯ СОЗДАНИЕ ТАБЛИЦЫ АККАУНТОВ ДЛЯ ОТКРЫТОГО ГОЛОСОВАНИЯ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_open_account)
        cursor.close()
        conn.close()
        return True

    def create_table_open_voting(self):
        #ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦЫ ОТКРЫТЫХ ГОЛОСОВАНИЙ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_open_voting)
        cursor.close()
        conn.close()
        return True

    def create_table_open_voting_decision(self):
        # ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦЫ ГОЛОСОВ В ОТКРЫТОМ ГОЛОСОВАНИИ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_open_voting_decision)
        cursor.close()
        conn.close()
        return True

    def create_table_close_account(self):
        # ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦЫ АККАУНТОВ ДЛЯ ЗАКРЫТОГО ГОЛОСОВАНИЯ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_close_account)
        cursor.close()
        conn.close()
        return True

    def create_table_close_voting(self):
        # ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦЫ ЗАКРЫТЫХ ГОЛОСОВАНИЙ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_close_voting)
        cursor.close()
        conn.close()
        return True

    def create_table_close_voting_decision(self):
        # ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦЫ ГОЛОСОВ В ЗАКРЫТОМ ГОЛОСОВАНИИ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute(permanent.create_table_close_voting_decision)
        cursor.close()
        conn.close()
        return True

    def create_roles(self):
        # ФУНКЦИЯ ЗАПОЛНЕНИЯ ТАБЛИЦЫ РОЛЕЙ
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO roles(role) VALUES (?)''', ('Студент',))
            cursor.execute('''INSERT INTO roles(role) VALUES (?)''', ('Аспирант',))
            cursor.execute('''INSERT INTO roles(role) VALUES (?)''', ('ППС',))
            cursor.execute('''INSERT INTO roles(role) VALUES (?)''', ('ППС, член УСУ',))
        except:
            pass
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def add_admin(self, fio, OKo):
        # ФУНКЦИЯ ДОБАВЛЕНИЯ АДМИНИСТРАТОРОВ
        # :ПАРАМЕТР fio - ФИО администратора
        # :ПАРАМЕТР OKo - открытый ключ администратора к аккаунту управления
        try:
            conn = sqlite3.connect('DatBas')
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO open_account(fio, OKo, admin) VALUES (?,?,?)''', (fio, OKo, 1,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            pass


#
    def add_open_user(self, fio, role, OKo):
        # ФУНКЦИЯ ДОБАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ В ТАБЛИЦУ АККАУНТОВ ДЛЯ ОТКРЫТОГО ГОЛОСОВАНИЯ
        # :ПАРАМЕТР fio - ФИО пользователя
        # :ПАРАМЕТР role - роль пользователя в системе
        # :ПАРАМЕТР OKo - открытый ключ пользователя к аккаунту для открытого голосования
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO open_account(fio, role, OKo) VALUES (?,?,?)''', (fio, role, OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
#
    def add_close_user(self, role, OKz):
        # ФУНКЦИЯ ДОБАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ В ТАБЛИЦУ АККАУНТОВ ДЛЯ ЗАКРЫТОГО ГОЛОСОВАНИЯ
        # :ПАРАМЕТР role - роль пользователя в системе
        # :ПАРАМЕТР OKz - открытый ключ пользователя к аккаунту для закрытого голосования
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO close_account(role, OKz) VALUES (?,?)''', (role, OKz,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
#
    def change_role(self, OKo, shift):
        # ФУНКЦИЯ ИЗМЕНЕНИЯ РОЛИ ПОЛЬЗОВАТЕЛЯ В СИСТЕМЕ
        # :ПАРАМЕТР OKz - открытый ключ пользователя к аккаунту для открытого голосования
        # :ПАРАМЕТР shift - изменение роли
        row = self.get_role_by_OKo(OKo)
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''UPDATE open_account SET role = (?) WHERE OKo = (?)''', ((row+shift), OKo,))
        conn.commit()
        if row == 2:
            cursor.execute('''UPDATE open_account SET IK = (?) WHERE OKo = (?)''', (None, OKo,))
        cursor.close()
        conn.close()
        return True
#
    def go_to_IK(self, OKo):
        # ФУНКЦИЯ ЗАПИСИ ПОЛЬЗОВАТЕЛЯ В ИЗБИРАТЕЛЬНУЮ КОМИССИЮ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        row = self.get_role_by_OKo(OKo)
        row = int((row+1)/2)
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''UPDATE open_account SET IK = (?) WHERE OKo = (?)''', (row, OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
#
    def go_out_IK(self, OKo):
        # ФУНКЦИЯ ИСКЛЮЧЕНИЯ ПОЛЬЗОВАТЕЛЯ ИЗ ИЗБИРАТЕЛЬНОЙ КОМИССИИ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''UPDATE open_account SET IK = (?) WHERE OKo = (?)''', (None, OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
#
    def delete_user(self, OKo):
        # ФУНКЦИЯ УДАЛЕНИЯ ПОЛЬЗОВАТЕЛЯ ИЗ СИСТЕМЫ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM open_account WHERE OKo = (?)''', (OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
#
    def to_be_auditor(self, OKo):
        # ФУНКЦИЯ НАЗНАЧЕНИЯ ПОЛЬЗОВАТЕЛЯ АУДИТОРОМ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        row =  self.get_role_by_OKo(OKo)
        au = 0
        if row == 1 or row == 2: au = 2
        elif row == 3 or row == 4: au = 1
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''UPDATE open_account SET auditor = (?) WHERE OKo = (?)''', (au, OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
#
    def not_to_be_auditor(self, OKo):
        # ФУНКЦИЯ ИСКЛЮЧЕНИЯ ПОЛЬЗОВАТЕЛ ИЗ ЧИСЛА АУДИТОРОВ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        row = self.get_role_by_OKo(OKo)
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''UPDATE open_account SET auditor = (?) WHERE OKo = (?)''', ('NULL', OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def change_personal_data(self, OKo, telephone, address):
        # ФУНКЦИЯ ИЗМЕНЕНИЯ ПЕРСОНАЛЬНЫХ ДАННЫХ ПОЛЬЗОВАТЕЛЯ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        # :ПАРАМЕТР telephone - новый номер телефона пользователя
        # :ПАРАМЕТР address - новый адрес проживания пользователя
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''UPDATE open_account SET telephone = (?), address = (?) WHERE OKo = (?)''', (telephone, address, OKo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def create_open_voting(self, OKo, candidate_OKo, day, month, year, during):
        # ФУНКЦИЯ СОЗДАНИЯ ОТКРЫТОГО ГОЛОСОВАНИЯ
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        # :ПАРАМЕТР candidate_OKo - открытый ключ пользователя, для которого предназначено голосование
        # :ПАРАМЕТР day - день начала голосования
        # :ПАРАМЕТР month - месяц голосования
        # :ПАРАМЕТР year - год голосования
        # :ПАРАМЕТР during - длительноть голосования в днях
        start = datetime(year = year, month = month, day = day)
        during = timedelta(days = during)
        finish = start + during
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        role = int(self.get_role_by_OKo(OKo))
        "1 - Назначить в ИК; 2 - Исключить из ИК"
        if OKo == candidate_OKo:
            question = 1
        else:
            question = 2
        cursor.execute('''INSERT INTO open_voting(question, role, candidate_OKo, start, finish) VALUES (?,?,?,?,?)''', (question, role, candidate_OKo, start, finish,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def create_close_voting(self, role, question, day, month, year, during):
        # ФУНКЦИЯ СОЗДАНИЯ ЗАКРЫТОГО ГОЛОСОВАНИЯ
        # :ПАРАМЕТР role - роль пользователей, для которых предназначено голосование
        # :ПАРАМЕТР question - список вопросов для голосования
        # :ПАРАМЕТР day - день начала голосования
        # :ПАРАМЕТР month - месяц голосования
        # :ПАРАМЕТР year - год голосования
        # :ПАРАМЕТР during - длительноть голосования в днях
        start = datetime(year=year, month=month, day=day)
        during = timedelta(days=during)
        finish = start + during
        question = json.dumps(question)
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO close_voting(role, question, start, finish) VALUES (?, ?, ?, ?)''', (role, question, start, finish))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def make_open_choice(self, id_voting, OKo, answer):
        # ФУНКЦИЯ ОТДАЧИ ГОЛОСА В ОТКРЫТОМ ГОЛОСОВАНИИ
        # :ПАРАМЕТР id_voting - уникальный номер голосования
        # :ПАРАМЕТР OKо - открытый ключ пользователя к аккаунту для открытого голосования
        # :ПАРАМЕТР answer - вариант, за который отдается голос
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO open_voting_decision(ID_gol, OKo, answer) VALUES(?,?,?)''', (id_voting, OKo, answer,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def make_close_choice(self, id_voting, OKz, answer):
        # ФУНКЦИЯ ОТДАЧИ ГОЛОСА В ЗАКРЫТОМ ГОЛОСОВАНИИ
        # :ПАРАМЕТР id_voting - уникальный номер голосования
        # :ПАРАМЕТР OKz - открытый ключ пользователя к аккаунту для закрытого голосования
        # :ПАРАМЕТР answer - вариант, за который отдается голос
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO close_voting_decision(ID_gol, OKz, answer) VALUES (?,?,?)''',(id_voting, OKz, answer,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def calculate_open_decision(self, id_vouting):
        # ФУНКЦИЯ ПОДСЧЕТА ГОЛОСОВ В ОТКРЫТОМ ГОЛОСОВАНИИ
        # :ПАРАМЕТР id_voting - уникальный номер голосования
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        proc = 0
        result = 0
        cursor.execute('''SELECT * FROM open_voting_decision WHERE id_gol = (?) AND answer = (?)''', (id_vouting, 1,))
        proc = len(cursor.fetchall())
        cursor.execute('''SELECT role FROM open_voting WHERE id = (?)''', (id_vouting,))
        role = cursor.fetchone()
        role = int(role[0])
        cursor.execute('''SELECT * FROM open_account WHERE role = (?) OR role = (?)''', ((role+1), (role+2)))
        members = len(cursor.fetchall())
        percent = proc / members * 100
        if percent > 51:
            result = 1
        else:
            result = 0
        cursor.execute('''UPDATE open_voting SET result = (?) WHERE id = (?)''', (result, id_vouting, ))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def calculate_close_decision(self, id_vouting):
        # ФУНКЦИЯ ПОДСЧЕТА ГОЛОСОВ В ЗАКРЫТОМ ГОЛОСОВАНИИ
        # :ПАРАМЕТР id_voting - уникальный номер голосования
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        proc = 0
        result = {}
        cursor.execute('''SELECT question FROM close_voting WHERE id = (?)''', (id_vouting,))
        question = cursor.fetchone()[0]
        question = json.loads(question)
        for i in range(1, len(question)):
            cursor.execute('''SELECT * FROM close_voting_decision WHERE id_gol = (?) AND answer = (?)''',
                           (id_vouting, i,))
            proc = cursor.fetchall()
            proc = len(proc)
            result.update({question[i]: proc})
        result = json.dumps(result)
        cursor.execute('''UPDATE close_voting SET result = (?) WHERE id = (?)''', (result, id_vouting,))
        conn.commit()
        cursor.close()
        conn.close()




    def get_roles(self):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT role FROM roles''')
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_role_by_OKo(self, OKo):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''SELECT role FROM open_account WHERE OKo = (?)''', (OKo,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return int(row[0])

    def get_role_by_OKz(self, OKz):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''SELECT role FROM close_account WHERE OKz = (?)''', (OKz,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return int(row[0])

    def get_user_by_OKo(self, OKo):
        try:
            conn = sqlite3.connect('DatBas')
            cursor = conn.cursor()
            row = {}
            cursor.execute('''SELECT fio FROM open_account WHERE OKo = (?)''', (OKo,))
            row = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return row
        except:
            return 0

    def get_user_by_role(self, role):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT fio FROM open_account WHERE role = (?)''', (role,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_OKo_by_user(self, fio):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''SELECT OKo FROM open_account WHERE fio = (?)''', (fio,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0]

    def get_active_open_voting(self, OKo):
        role = self.get_role_by_OKo(OKo)
        now = datetime.now()
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT * FROM open_voting WHERE role = (?) AND start < (?) AND finish > (?)''', (role, now, now,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_finished_open_voting(self):
        now = datetime.now()
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT id FROM open_voting WHERE finish < (?)''',(now,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_finished_open_voting_results(self, id_gol):
        now = datetime.now()
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT question, candidate_OKo, result FROM open_voting WHERE id = (?)''',(id_gol,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_active_close_voting(self, OKz):
        role = self.get_role_by_OKz(OKz)
        now = datetime.now()
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT * FROM close_voting WHERE role = (?) AND start < (?) AND finish > (?)''', (int((role+1)/2), now, now,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_finished_close_voting(self):
        now = datetime.now()
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT * FROM close_voting WHERE finish < (?)''',(now,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_finished_close_voting_results(self, id_gol):
        now = datetime.now()
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT question, result FROM open_voting WHERE id = (?)''',(id_gol,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_admins(self):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT OKo FROM open_account WHERE admin = (?)''', (1,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_close_users(self):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT OKz FROM close_account''')
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_IK_by_OKo(self, OKo):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.execute('''SELECT IK FROM open_account WHERE OKo = (?)''', (OKo,))
        row = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return row

    def get_auditor_by_OKo(self, OKo):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.execute('''SELECT auditor FROM open_account WHERE OKo = (?)''', (OKo,))
        row = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return row

    def get_time_from_open_vouting(self, id_vot):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.execute('''SELECT start FROM open_voting WHERE id = (?)''', (id_vot,))
        row = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return row

    def get_time_from_close_vouting(self, id_vot):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.execute('''SELECT start FROM close_voting WHERE id = (?)''', (id_vot,))
        row = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return row

    def get_ID_role_by_role(self, role):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''SELECT id_role FROM roles WHERE role = (?)''', (role,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0]

    def get_users(self):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        row = {}
        cursor.row_factory = dict_factory
        cursor.execute('''SELECT fio FROM open_account''')
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_ID_vot_by_question(self, question):
        conn = sqlite3.connect('DatBas')
        cursor = conn.cursor()
        cursor.execute('''SELECT id FROM open_voting WHERE question = (?)''', (question,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0]