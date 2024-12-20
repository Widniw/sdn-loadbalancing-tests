#!/usr/bin/python

from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo
from mininet.link import TCLink

class FatTree(Topo):

    "Fat Tree Topology"

    def __init__(self):
        "Create Fat tree Topology"

        Topo.__init__(self)

        #Add hosts
        h7 = self.addHost('h7', cls=Host, ip='10.0.0.7')
        h8 = self.addHost('h8', cls=Host, ip='10.0.0.8')
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1')
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2')
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4')
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3')
        h5 = self.addHost('h5', cls=Host, ip='10.0.0.5')
        h6 = self.addHost('h6', cls=Host, ip='10.0.0.6')

        #Add switches
        s10 = self.addSwitch('s10', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s17 = self.addSwitch('s17', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)
        s18 = self.addSwitch('s18', cls=OVSKernelSwitch)
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s11 = self.addSwitch('s11', cls=OVSKernelSwitch)
        s21 = self.addSwitch('s21', cls=OVSKernelSwitch)
        s22 = self.addSwitch('s22', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)

        #Add links
        self.addLink(h1, s1, cls=TCLink)
        self.addLink(h2, s1, cls=TCLink)
        self.addLink(h3, s2, cls=TCLink)
        self.addLink(h4, s2, cls=TCLink)
        self.addLink(h5, s3, cls=TCLink)
        self.addLink(h6, s3, cls=TCLink)
        self.addLink(h7, s4, cls=TCLink)
        self.addLink(h8, s4, cls=TCLink)
        self.addLink(s1, s21, cls=TCLink)
        self.addLink(s21, s2, cls=TCLink)
        self.addLink(s1, s10, cls=TCLink)
        self.addLink(s2, s10, cls=TCLink)
        self.addLink(s3, s11, cls=TCLink)
        self.addLink(s4, s22, cls=TCLink)
        self.addLink(s11, s4, cls=TCLink)
        self.addLink(s3, s22, cls=TCLink)
        self.addLink(s21, s17, cls=TCLink)
        self.addLink(s11, s17, cls=TCLink)
        self.addLink(s10, s18, cls=TCLink)
        self.addLink(s22, s18, cls=TCLink)

topos = { 'FatTree': (lambda: FatTree() ) }