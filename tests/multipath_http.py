from topologies.multipath import Multipath
from tests.utils import set_http_server, transfer_file_http
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController, Node
from mininet.cli import CLI
import time
import threading

def run_test():
    topo = Multipath()
    controller = RemoteController(name = 'c0',ip = '127.0.0.1', port = 6653)
    net = Mininet(topo = topo, controller = controller, autoSetMacs = True)
    net.start()

    # For STP to construct a tree
    time.sleep(35)
    
    h1 = net.get('h1')
    h1.pexec('dd if=/dev/zero of=/tmp/testfile bs=1M count=100')        

    h2 = net.get('h2')
    h2.pexec('dd if=/dev/zero of=/tmp/testfile bs=1M count=100')      
    
    h3 = net.get('h3')
    h3.pexec('dd if=/dev/zero of=/tmp/testfile bs=1M count=100')

    h4 = net.get('h4')
    h4.pexec('dd if=/dev/zero of=/tmp/testfile bs=1M count=100')      

    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')

    print("Starting parallel HTTP transfers:")

    set_http_server(h1)
    set_http_server(h2)
    set_http_server(h3)
    set_http_server(h4)

    time.sleep(5)

    t1 = threading.Thread(target=transfer_file_http, args=(h1, h5, 'testfile_h5'))
    t2 = threading.Thread(target=transfer_file_http, args=(h2, h6, 'testfile_h6'))
    t3 = threading.Thread(target=transfer_file_http, args=(h3, h7, 'testfile_h7'))
    t4 = threading.Thread(target=transfer_file_http, args=(h4, h8, 'testfile_h8'))


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_test()