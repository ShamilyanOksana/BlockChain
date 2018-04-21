import socket
import json
import DatabaseIP
import Blockchain
from EncDec import enc, dec


class Network:

    def get_message(self):
        while True:
            sock = socket.socket()
            HOST = socket.gethostname()

            sock.bind(('', 9090))
            sock.listen(1)
            conn, address = sock.accept()
            self.add_new_ip(address[0])
            package = conn.recv(32768)
            if package:
                Blockchain.BlockChain(package)
            sock.close()

    def send_message(self, data):
        hostname = socket.gethostname()
        my_ip = socket.gethostbyname(hostname)
        self.add_new_ip(my_ip)
        ip_list = self.get_all_ip()
        for ip in ip_list:
            ip = ip.get('ip')
            sock = socket.socket()
            try:
                sock.settimeout(5)
                sock.connect((ip, 9090))
                sock.send(data)
                sock.settimeout(None)
                sock.close()
            except Exception:
                sock.close()

    def add_new_ip(self, ip):
        try:
            db = DatabaseIP.DataBaseIP()
            db.add_ip(ip)
        except Exception:
            pass

    def get_all_ip(self):
        db = DatabaseIP.DataBaseIP()
        ip_list = db.get_ip_list()
        return ip_list

    def send_to_user(self, ip, data):
        sock = socket.socket()
        try:
            sock.settimeout(5)
            sock.connect((ip, 9090))
            sock.send(data)
            sock.settimeout(None)
            sock.close()
        except Exception:
            sock.close()