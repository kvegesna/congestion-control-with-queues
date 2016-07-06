#!/usr/bin/python

"""
Simple example of setting network and CPU parameters

NOTE: link params limit BW, add latency, and loss.
There is a high chance that pings WILL fail and that
iperf will hang indefinitely if the TCP handshake fails
to complete.
"""

from __future__ import print_function

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

from sys import argv

class TwoSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, lossy=True, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            if lossy:
                # 10 Mbps, 5ms delay, 10% packet loss
                if h <= (n/2):
                    self.addLink(host, switch,
                    bw=10, delay='5ms', loss=10, use_htb=True)
                else:
                    self.addLink(host, switch2,
                    bw=10, delay='5ms', loss=10, use_htb=True)
            else:
                # 10 Mbps, 5ms delay, no packet loss
                if h <= (n/2):
                    self.addLink(host, switch,
                    bw=10, delay='5ms', loss=10, use_htb=True)
                else:
                    self.addLink(host, switch2,
                    bw=10, delay='5ms', loss=10, use_htb=True)


def BwidthTest( lossy=True ):
    "Create network and run simple performance test"
    topo = TwoSwitchTopo( n=4, lossy=lossy )
    net = Mininet( topo=topo,
                   host=CPULimitedHost, link=TCLink,
                   autoStaticArp=True )
    net.start()
    print( "Dumping host connections" )
    dumpNodeConnections(net.hosts)
    print( "Testing throughput between h1 and h4" )
    h1, h4 = net.getNodeByName('h1', 'h4')
    net.iperf( ( h1, h4 ), l4Type='UDP' )
    print( "Testing throughput between h1 and h3" )
    h1, h3 = net.getNodeByName('h1', 'h3')
    net.iperf( ( h1, h3 ), l4Type='UDP' )
    print( "Testing throughput between h2 and h4" )
    h2, h4 = net.getNodeByName('h2', 'h4')
    net.iperf( ( h2, h4 ), l4Type='UDP' )
    print( "Testing throughput between h2 and h3" )
    h2, h3 = net.getNodeByName('h2', 'h3')
    net.iperf( ( h2, h3 ), l4Type='UDP' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    # Prevent test_simpleperf from failing due to packet loss
    BwidthTest( lossy=( 'testmode' not in argv ) )
