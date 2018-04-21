import threading
from Network import Network
import Mining

listerning = threading.Thread(name = 'serwer', target = Network.get_message)

mining = threading.Thread(name = 'miner', target = )


