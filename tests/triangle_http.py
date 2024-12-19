from topologies.triangle import Triangle
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController, Node
from mininet.cli import CLI
from utils import set_http_server, transfer_file_http
import time
import threading

# def _set_http_server(host: Node):
#     output = host.cmd('python3 -m http.server 8000 -d / &')

#     print(f'Set server info: {output}')

# def set_http_server(host:Node):
#     server_thread = threading.Thread(target = _set_http_server, args = (host,))
#     server_thread.start()

# def transfer_file_http(src_host: Node, dest_host: Node, dest_filename):
#     # Measure transfer time with curl
#     start_time = time.time()
#     output = dest_host.pexec(f'curl http://{src_host.IP()}:8000/tmp/testfile -o /tmp/{dest_filename}')
#     end_time = time.time()
    
#     duration = end_time - start_time
#     print(f'{output = }')
#     print(f"Transfer from {src_host} to {dest_host} completed in {duration:.2f} seconds")

def run_test():
    topo = Triangle()
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

    h4 = net.get('h4')
    h4.pexec('dd if=/dev/zero of=/tmp/testfile bs=1M count=100')      

    h5 = net.get('h5')


    print("Starting parallel HTTP transfers:")

    set_http_server(h4)
    set_http_server(h2)
    set_http_server(h1)

    time.sleep(7)

    t1 = threading.Thread(target=transfer_file_http, args=(h4, h5, 'testfile_h1_to_h2'))
    t2 = threading.Thread(target=transfer_file_http, args=(h2, h3, 'testfile_h2_to_h3'))
    t3 = threading.Thread(target=transfer_file_http, args=(h1, h2, 'testfile_h1_to_h3'))

    threads_list = [t1, t2, t3]

    for thread in threads_list:
        thread.start()

    for thread in threads_list:
        thread.join()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_test()