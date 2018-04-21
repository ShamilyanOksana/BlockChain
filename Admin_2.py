# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import data_basa
import json
import Network
import rsa
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 380, 180, 228))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 380, 195, 128))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 380, 180, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(660, 330, 251, 241))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_4)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(15, 199, 381, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 380, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(630, 90, 191, 81))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(630, 200, 411, 91))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #------------------------Сигналы Слоты------------------------
        self.pushButton_11.clicked.connect(self.getUser)
        self.pushButton.clicked.connect(self.addUser)
        #self.pushButton_4.clicked.connect(self.Test_Combo_Box) Test Combo Box
        self.pushButton_4.clicked.connect(self.Create_UP_Role)
        self.pushButton_5.clicked.connect(self.Create_Down_Role)
        self.pushButton_6.clicked.connect(self.Create_Add_to_IK)
        self.pushButton_7.clicked.connect(self.Create_Delete_IK)
        self.pushButton_10.clicked.connect(self.Create_Trans_In_Auditor)
        self.pushButton_9.clicked.connect(self.Create_Trans_Delate_Auditor)
        self.pushButton_2.clicked.connect(self.Create_Trans_Dealate_User)
        # self.pushButton_8.clicked.connect(self.Clear_Users_Spisok)
        self.BASA=data_basa.Basa()
        self.getRoles()






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Админ ЦУУ"))
        self.pushButton_4.setText(_translate("MainWindow", "Повысить должность"))
        self.pushButton_5.setText(_translate("MainWindow", "Понизить должность"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить в ИК"))
        self.pushButton_7.setText(_translate("MainWindow", "Ислючить из ИК"))
        self.pushButton_10.setText(_translate("MainWindow", "Назначить аудитором"))
        self.pushButton_9.setText(_translate("MainWindow", "Удалить аудитора"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить пользователя"))
        self.radioButton_2.setText(_translate("MainWindow", "Отоброзить преподователей"))
        self.radioButton.setText(_translate("MainWindow", "Отоброзить студентов"))
        self.pushButton_11.setText(_translate("MainWindow", "Отоброзить"))
        self.label_6.setText(_translate("MainWindow", "Пользователи"))
        self.label_7.setText(_translate("MainWindow", "Доступные Голосования"))
        self.pushButton_8.setText(_translate("MainWindow", "Отоброзить"))
        self.label_8.setText(_translate("MainWindow", "Уведомления о регистрациях"))
        self.pushButton_3.setText(_translate("MainWindow", "Отоброзить уведомления"))
        self.label_4.setText(_translate("MainWindow", "Добавить в открытое голосование"))
        self.label_5.setText(_translate("MainWindow", "Должность"))
        self.pushButton.setText(_translate("MainWindow", "Зарегистрировать"))
        self.label_2.setText(_translate("MainWindow", "ФИО"))
        self.label_3.setText(_translate("MainWindow", "Открытый Ключ"))
        self.label_9.setText(_translate("MainWindow", "Добавить в закрытое голосование"))
        self.label_10.setText(_translate("MainWindow", "Открытый Ключ"))
        self.label_11.setText(_translate("MainWindow", "Должность"))
        self.pushButton_14.setText(_translate("MainWindow", "Зарегистрировать"))
    def getUser(self):
        #Пока не работает
        if self.radioButton.isChecked() == True:
            self.comboBox.clear()
            numberRole = int(1)
            massData = self.BASA.get_user_by_role(numberRole)

            for i in range(len(massData)):
                self.plainTextEdit.appendPlainText(massData[i].get("fio"))
                self.comboBox.addItem(massData[i].get("fio"))
        if self.radioButton_2.isChecked()==True:
            self.comboBox.clear()
            numberRole = int(2)
            massData = self.BASA.get_user_by_role(numberRole)
            for i in range(len(massData)):
                self.comboBox.addItem(massData[i].get("fio"))
    def addUser(self):
        fio = self.lineEdit.text()
        openKey  = self.lineEdit_2.text()
        role = self.comboBox_3.currentText()
        self.BASA.add_open_user(fio,role,openKey)

    def getRoles(self):
        temp = self.BASA.get_roles()
        for i in range(len(temp)):
            self.comboBox_3.addItem(temp[i].get('role'))
            self.comboBox_4.addItem(temp[i].get('role'))
    def Test_Combo_Box(self):#Работа с Combo Boxom
        self.a =  self.comboBox_3.currentText()
        self.plainTextEdit.appendPlainText(self.a)
    def Create_Trans_to_Add_Open_User(self):
        NumberTransaction = 1
        fio1 = self.lineEdit.text()
        OKey = self.lineEdit_2.text()
        Dloznoststr = self.comboBox_3.currentText()
        Dolznost=self.BASA.get_ID_role_by_role(Dloznoststr)
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        transaction = {}
        data = {}
        data.update({'fio':fio1})
        data.update({'OKo':OKey})
        data.update({'role':Dolznost})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code':NumberTransaction})
        transaction.update({'data':data})
        transaction.update({'sign':signature})
        transaction = json.dumps(transaction)

    def Create_Trans_to_Add_Closd_User(self):
        NumberTransacton = 2
        Okey = self.lineEdit_3.text()
        Role = self.comboBox_4.currentText()
        Dolznost=self.BASA.get_ID_role_by_role(Role)
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        data = {}
        transaction = {}
        data.update({'OKz':Okey})
        data.update({'role':Dolznost})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'code': NumberTransacton})
        transaction.update({'data': data})
        s = rsa.sign(transaction)
        transaction.update({'type': 'transaction'})

        transaction.update({'sign': signature})

        transaction = json.dumps(transaction, sort_keys=True)
        transaction = transaction.encode()
        Network.Network().send_message(transaction)

    def Create_UP_Role(self):
        NumberTransaction =3
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        data = {}
        transaction = {}
        data.update({'OKo':userOk})
        data.update({'shift': 1})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})
    def Create_Down_Role(self):
        NumberTransaction = 4
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        data = {}
        transaction = {}
        data.update({'OKo': userOk})
        data.update({'shift': -1})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})
    def Create_Add_to_IK(self):
        NumberTransaction = 5
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        self.plainTextEdit.appendPlainText(userOk)
        data = {}
        transaction = {}
        data.update({'OKo':userOk})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})
    def Create_Delete_IK(self):
        NumberTransaction = 6
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        data = {}
        transaction = {}
        data.update({'OKo': userOk})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})
    def Create_Trans_In_Auditor(self):
        NumberTransaction = 7
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        data = {}
        transaction = {}
        data.update({'OKo': userOk})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})
    def Create_Trans_Delate_Auditor(self):
        NumberTransaction = 8
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        data = {}
        transaction = {}
        data.update({'OKo': userOk})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})
    def Create_Trans_Dealate_User(self):
        NumberTransaction = 9
        AdminKey = 'Test_Key112233445566778899aabbcc'
        signature = 'Test_Signature'
        UserName = self.comboBox.currentText()
        userOk = self.BASA.get_OKo_by_user(UserName)
        data = {}
        transaction = {}
        data.update({'OKo': userOk})
        data = json.dumps(data)
        transaction.update({'ok': AdminKey})
        transaction.update({'type': 'transaction'})
        transaction.update({'code': NumberTransaction})
        transaction.update({'data': data})
        transaction.update({'sign': signature})




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

