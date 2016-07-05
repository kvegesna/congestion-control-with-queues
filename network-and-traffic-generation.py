#!/usr/bin/python

"""
Creation of a network with numerous hosts and 1 switch. The aim is to create network congestion with a lot of traffic flow. I have two types of traffic: TCP and UDP! 
"""

from __future__ import print_function

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


from sys import argv

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)



def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( n=4,)
    net = Mininet( topo=topo,
                   host=CPULimitedHost, link=TCLink,
                   autoStaticArp=True )
    net.start()
    print( "Dumping host connections" )
    dumpNodeConnections(net.hosts)
    print( "Testing throughput between hosts" )
    h1, h4 = net.getNodeByName('h1', 'h4')
    net.iperf( ( h1, h4 ), l4Type='UDP', udpBw='1000M')
    net.iperf( ( h1, h4 ), l4Type='TCP' )
    h1, h3 = net.getNodeByName('h1', 'h3')
    net.iperf( ( h1, h3 ), l4Type='UDP' )
    net.iperf( ( h1, h3 ), l4Type='TCP' )
    h1, h2 = net.getNodeByName('h1', 'h2')
    net.iperf( ( h1, h2 ), l4Type='UDP' )
    net.iperf( ( h1, h2 ), l4Type='TCP' )

    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    perfTest( )
