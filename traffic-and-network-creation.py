#!/usr/bin/python
# Karthik Vegesna 

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
    print( "Testing throughput between h1 and h4" )
    h1, h4 = net.getNodeByName('h1', 'h4')
    h4.popen("iperf -s -u", shell = True)
    h3.popen("iperf -s -u", shell = True)
    h2.popen("iperf -s -u", shell = True)
    h1.popen("iperf -c -u", shell = True)
    process  = h1.popen("iperf -u -s 10.0.0.4 -p 5001 -t 1", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    print( "Testing throughput between h1 and h3" )
    process  = h1.popen("iperf -u -s 10.0.0.3 -p 5001 -t 1", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    print( "Testing throughput between h1 and h2" )
    h1, h2 = net.getNodeByName('h1', 'h2')
    h2.popen("iperf -s -u", shell = True)
    process  = h1.popen("iperf -u -s 10.0.0.2 -p 5001 -t 1", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    # Prevent test_simpleperf from failing due to packet loss
    BwidthTest( lossy=( 'testmode' not in argv ) )

