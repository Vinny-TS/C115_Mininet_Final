# -*- coding: utf-8 -*-

from mininet.topo import Topo

class CustomTopo( Topo ):
    def build( self ):
        # Adicionando os Hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )

        # Adicionando os Switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s7 = self.addSwitch( 's7' )

        # Links do s1 para os switches de borda
        self.addLink( s1, s2 ) # s1-eth1 <-> s2-eth1
        self.addLink( s1, s3 ) # s1-eth2 <-> s3-eth1
        self.addLink( s1, s7 ) # s1-eth3 <-> s7-eth1

        # Links dos hosts para o s2
        self.addLink( s2, h1 ) # s2-eth2 <-> h1-eth0
        self.addLink( s2, h2 ) # s2-eth3 <-> h2-eth0
        
        # Link do host para o s3
        self.addLink( s3, h3 ) # s3-eth2 <-> h3-eth0
        
        # Links dos hosts para o s7
        self.addLink( s7, h4 ) # s7-eth2 <-> h4-eth0
        self.addLink( s7, h5 ) # s7-eth3 <-> h5-eth0
        self.addLink( s7, h6 ) # s7-eth4 <-> h6-eth0

topos = { 'mytopo': ( lambda: CustomTopo() ) }