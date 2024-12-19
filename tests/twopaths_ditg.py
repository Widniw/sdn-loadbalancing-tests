import argparse
from topologies.twopaths import Twopaths
from tests.utils import set_ditg_recv, set_ditg_send
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController, Node
from mininet.cli import CLI
from typing import List
import time
import threading

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Run a Mininet test with a specified algorithm name for logging."
    )
    parser.add_argument(
        "--algorithm",
        type=str,
        required=True,
        help="The algorithm name used for logging files."
    )
    return parser.parse_args()

def run_test(algorithm: str):
    topo = Twopaths()
    controller = RemoteController(name='c0', ip='127.0.0.1', port=6653)
    net: Mininet = Mininet(topo=topo, controller=controller, autoSetMacs = True)
    net.start()

    time.sleep(30)
    net.pingAllFull()

    senders = ['h1', 'h2']
    receivers = ['h3', 'h4']

    for receiver_name in receivers:
        receiver: Node = net.get(receiver_name)
        set_ditg_recv(receiver)

    threads: List[threading.Thread] = []

    for index, sender_name in enumerate(senders):
        sender: Node = net.get(sender_name)
        receiver_name = receivers[index]
        receiver: Node = net.get(receiver_name)

        threads.append(threading.Thread(target=set_ditg_send, args=(sender, receiver, algorithm)))

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    args = parse_arguments()
    setLogLevel('info')
    run_test(args.algorithm)
