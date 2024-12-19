from mininet.node import Node
import threading
import time


def _set_http_server(host: Node):
    output = host.cmd('python3 -m http.server 8000 -d / &')

    print(f'Set server info: {output}')

def set_http_server(host:Node):
    server_thread = threading.Thread(target = _set_http_server, args = (host,))
    server_thread.start()

def transfer_file_http(src_host: Node, dest_host: Node, dest_filename):
    start_time = time.time()
    output = dest_host.pexec(f'curl http://{src_host.IP()}:8000/tmp/testfile -o /tmp/{dest_filename}')
    end_time = time.time()
    
    duration = end_time - start_time
    print(f'{output = }')
    print(f"Transfer from {src_host} to {dest_host} completed in {duration:.2f} seconds")

def _set_ditg_recv(host: Node):
    output = host.pexec(f'sudo /home/krzysiek/inzynierka/D-ITG/D-ITG-2.8.1-r1023/bin/ITGRecv')
    print(f'recv output for {host.name}: {output}')

def set_ditg_recv(host: Node):
    server_thread = threading.Thread(target=_set_ditg_recv, args=(host,))
    server_thread.start()
    time.sleep(1)
    output = host.pexec(f'sudo netstat -tuln | grep 9000')
    print(f'Recv state on {host}: {output}')

def set_ditg_send(sender: Node, receiver: Node, algorithm: str):
    output = sender.pexec(
        f'sudo /home/krzysiek/inzynierka/D-ITG/D-ITG-2.8.1-r1023/bin/ITGSend'
        f' -T TCP -a {receiver.IP()} -k 100000 -C 8333 -c 1500'
        f' -l D-ITG-logs/{algorithm}_sender{sender.name}.log'
        f' -x D-ITG-logs/{algorithm}_receiver{receiver.name}.log -m rttm'
    )
    print(f'{output = }')