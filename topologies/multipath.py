#!/usr/bin/python

from mininet.node import Host 
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo
from mininet.link import TCLink

class Multipath(Topo):

    def __init__(self):
        Topo.__init__(self)

        #Add hosts
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1')
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2')
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3')
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4')
        h5 = self.addHost('h5', cls=Host, ip='10.0.0.5')
        h6 = self.addHost('h6', cls=Host, ip='10.0.0.6')
        h7 = self.addHost('h7', cls=Host, ip='10.0.0.7')
        h8 = self.addHost('h8', cls=Host, ip='10.0.0.8')


        #Add switches
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)
        s5 = self.addSwitch('s5', cls=OVSKernelSwitch)
        s6 = self.addSwitch('s6', cls=OVSKernelSwitch)


        #Add links
        self.addLink(h1, s1, cls=TCLink, bw=100)
        self.addLink(h2, s1, cls=TCLink, bw=100)
        self.addLink(h3, s1, cls=TCLink, bw=100)
        self.addLink(h4, s1, cls=TCLink, bw=100)
        self.addLink(h5, s2, cls=TCLink, bw=100)
        self.addLink(h6, s2, cls=TCLink, bw=100)
        self.addLink(h7, s2, cls=TCLink, bw=100)
        self.addLink(h8, s2, cls=TCLink, bw=100)
        self.addLink(s3, s1, cls=TCLink, bw=100)
        self.addLink(s3, s2, cls=TCLink, bw=100)
        self.addLink(s4, s1, cls=TCLink, bw=100)
        self.addLink(s4, s2, cls=TCLink, bw=100)
        self.addLink(s5, s1, cls=TCLink, bw=100)
        self.addLink(s5, s2, cls=TCLink, bw=100)
        self.addLink(s6, s1, cls=TCLink, bw=100)
        self.addLink(s6, s2, cls=TCLink, bw=100)


topos = { 'multipath': (lambda: Multipath() ) }