'''
Created on Mar 26, 2013

@author: kavya
'''
class NodeID:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = int(port)
        
    @property
    def ip_addr(self):
        return self._ip_addr
    
    @property
    def port(self):
        return self._port
    
    