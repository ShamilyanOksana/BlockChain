import threading
import Network
import Maining
import DatabaseBC

DatabaseBC.DataBaseBC().create_table_block()
DatabaseBC.DataBaseBC().create_table_transaction()

net = Network.Network()
t1 = threading.Thread(name='server', target=net.get_message)
t1.start()

m = Maining.Maining()
t2 = threading.Thread(name='maining', target=m.collecting_block, args={m.block_size()})
t2.start()
