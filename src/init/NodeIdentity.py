'''
Created on Mar 26, 2013

@author: kavya
'''
class NodeID:
    _ip_addr = None
    _port = None
    _id = None
    
    
    def __init__(self, ip_addr, port, id):
        self.ip_addr = ip_addr
        self.port = int(port)
        self.id = id
        
    @property
    def ip_addr(self):
        return self._ip_addr
    
    @property
    def port(self):
        return self._port
    
    