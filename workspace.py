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
                    bw=10, delay='5ms', loss=0, use_htb=True)
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            if lossy:
                if h <= ((n/2) - 1):
                    self.addLink(host, switch,
                    bw=10, delay='5ms', loss=0, use_htb=True)
                else:
                    self.addLink(host, switch2,
                    bw=10, delay='5ms', loss=0, use_htb=True)
            else:
                # 10 Mbps, 5ms delay, no packet loss
                if h <= ((n/2)-1):
                    self.addLink(host, switch,
                    bw=10, delay='5ms', loss=0, use_htb=True)
                else:
                    self.addLink(host, switch2,
                    bw=10, delay='5ms', loss=0, use_htb=True)




def BwidthTest( lossy=True ):
    "Create network and run simple performance test"
    topo = TwoSwitchTopo( n=4, lossy=lossy )
    net = Mininet( topo=topo,
                   host=CPULimitedHost, link=TCLink,
                   autoStaticArp=True )
    net.start()
    f = open('output.txt','w')
    print( "Testing throughput between h1 and h4" )
    #Return node(s) with given name(s) 
    h1, h2, h3, h4 = net.getNodeByName('h1', 'h2','h3','h4')
    h4.popen("iperf -s -u", shell = True)
    processC=h4.popen("iperf -s -i 1", shell = True)
    #h3.popen("iperf -s -u", shell = True)
    #h2.popen("iperf -s -u", shell = True)
    #h1.popen("iperf -c -u", shell = True)
    processA  = h1.popen("iperf -c 10.0.0.4 -p 5001 -t 35 -i 1", shell=True)
    #processB  = h1.popen("iperf -c 10.0.0.4 -p 5001 -t 20 -i 1", shell =True)
    sleep(5)
    print( "Throughput between h1 and h4, bwidth of 2" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5001 -t 5 -b 2M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    f.write(stdout)
    print( "Throughput between h1 and h4, bwidth of 4" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5001 -t 5 -b 4M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    f.write(stdout)
    print( "Throughput between h1 and h4, bwidth of 6" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5001 -t 5 -b 6M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    f.write(stdout)
    print( "Throughput between h1 and h4, bwidth of 8" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5001 -t 5 -b 8M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    f.write(stdout)
    print( "Throughput between h1 and h4, bwidth of 10" )
    process  = h1.popen("iperf -u -c 10.0.0.4 -p 5001 -t 5 -b 10M", shell=True)
    stdout, stderr = process.communicate()
    print( stdout )
    f.write(stdout)
    stdout1, stderr1 = processA.communicate()
    print( stdout1 )
    #print( "error:", stderr1 )
    f.write(stdout1)
    #stdout2, stderr2 = processB.communicate()
    #print( stdout2 )
    #f.write(stdout2)
    d = processA.kill()
    stdout1, stderr1 = processC.communicate()
    print( stdout1 )
    f.close()
    net.stop()

if __name__ == '__main__':
  setLogLevel( 'info' )
    # Prevent test_simpleperf from failing due to packet loss
    BwidthTest( lossy=( 'testmode' not in argv ) )
                                                                                                  
