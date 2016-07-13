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
