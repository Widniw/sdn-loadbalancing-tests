#!/usr/bin/python
from mininet.node import Host 
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo
from mininet.link import TCLink

class Simple(Topo):

    def __init__(self):
        Topo.__init__(self)

        #Add hosts
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1')
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2')

        #Add switch
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)

        #Add links
        self.addLink(h1, s1, cls=TCLink, bw=100)
        self.addLink(h2, s1, cls=TCLink, bw=100)
 
topos = { 'simple': (lambda: Simple() ) }