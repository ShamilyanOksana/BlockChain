import Network
import sqlite3
import DatabaseBC
sync = {'type': 'synchronize'}
import socket


id = DatabaseBC.DataBaseBC().get_my_len()

sock = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

sync.update({'chain': id})
sync.update({'ip': ip})

net = Network.Network()

net.send_message(sync)
