#!/usr/bin/python
# Karthik Vegesna 

from __future__ import print_function
from time import sleep
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
import io

from sys import argv

class TwoSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, lossy=True, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')

        self.addLink(switch, switch2,
                    bw=5, delay='5ms', loss=0, use_htb=True, max_queue_size=25)
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            if lossy:
                if h <= ((n/2) - 1):
                    self.addLink(host, switch,
                    delay='5ms', loss=0, use_htb=True, max_queue_size=25)
                else:
                    self.addLink(host, switch2,
                    delay='5ms', loss=0, use_htb=True, max_queue_size=25)
            else:
                # 10 Mbps, 5ms delay, no packet loss
                if h <= ((n/2)-1):
                    self.addLink(host, switch,
                    delay='5ms', loss=0, use_htb=True, max_queue_size=25)
                else:
                    self.addLink(host, switch2,
                    delay='5ms', loss=0, use_htb=True, max_queue_size=25)
def BwidthTest( lossy=True ):
    "Create network and run simple performance test"
    topo = TwoSwitchTopo( n=4, lossy=lossy )
    net = Mininet( topo=topo,
                   host=CPULimitedHost, link=TCLink,
                   autoStaticArp=True )
    net.start()
    CLI(net)
    f = open('output.txt','w')
    print( "Testing throughput between h1 and h4" )
    #Return node(s) with given name(s) 
    h1, h2, h3, h4 = net.getNodeByName('h1', 'h2','h3','h4')
    #Creating a UDP Server on H4
    h4.popen("iperf -s -u", shell = True)
    #Creating a TCP Server for the long running TCP Process
    processC=h4.popen("iperf -s -p 5201 -i 1 -1", shell = True)
    processD=h4.popen("iperf -s -p 5202 -i 1", shell = True)
    processA  = h1.popen("iperf -c 10.0.0.4 -p 5201 -t 100 -i 1 -b 5M", shell=True)
    sleep(5)
    print( "Throughput between h1 and h4, bwidth of 2" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5202 -t 10 -b 2M", shell=True)
    stdout, stderr = process.communicate()
    #f.write(stdout)
    print( stdout)
    sleep(10)
    print( "Throughput between h1 and h4, bwidth of 4" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5202 -t 10 -b 4M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    #f.write(stdout)
    sleep(5)
    print( "Throughput between h1 and h4, bwidth of 6" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5202 -t 10 -b 6M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    sleep(5)
    print( "Throughput between h1 and h4, bwidth of 8" )
    process = h1.popen("iperf -u -c 10.0.0.4 -p 5202 -t 10 -b 8M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    sleep(5)
    stdout1, stderr1 = processC.communicate()
    print( stdout1 )
    f.write(stdout1)
    stdout2, stderr2 = processA.communicate()
    print( stdout2 )
    print ("hello")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    # Prevent test_simpleperf from failing due to packet loss
    BwidthTest( lossy=( 'testmode' not in argv ) )

                                                            
                                                                            
