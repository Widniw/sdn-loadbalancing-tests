#!/usr/bin/python

from mininet.node import Host 
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo
from mininet.link import TCLink

class Twopaths(Topo):

    def __init__(self):
        Topo.__init__(self)

        #Add hosts
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1')
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2')
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3')
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4')

        #Add switches
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)

        #Add links
        self.addLink(h1, s1, cls=TCLink, bw=100)
        self.addLink(h2, s1, cls=TCLink, bw=100)
        self.addLink(h3, s2, cls=TCLink, bw=100)
        self.addLink(h4, s2, cls=TCLink, bw=100)
        self.addLink(s1, s2, cls=TCLink, bw=100)
        self.addLink(s1, s3, cls=TCLink, bw=100)
        self.addLink(s3, s4, cls=TCLink, bw=100)
        self.addLink(s4, s2, cls=TCLink, bw=100)


topos = { 'twopaths': (lambda: Twopaths() ) }