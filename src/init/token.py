'''
Created on Mar 30, 2013

@author: apoorva
'''

class token:
    tokenId = None 
    IdtoIp = []
    #this will initialize both token_count and IdtoIp with proper values
    def token(self,arr,nlist):
        self.IdtoIp = arr
       
    #every time the token needs to be incremented it is checked against its IP 
    def checkValid(self,node):
        if self.IdtoIp[node.id] == node.ip_addr:
            if self.tokenId == node.id:
                return True
        return False