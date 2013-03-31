'''
Created on Mar 30, 2013

@author: apoorva
'''

class token:
    tokenCount = []
    IdtoIp = []
    #this will initialize both token_count and IdtoIp with proper values
    def token(self,arr,nlist):
        self.IdtoIp = arr
        #initialize the count values with 0
        for item in nlist:
            self.tokenCount[item.id] = 0
    #every time the token needs to be incremented it is checked against its IP 
    def incrementTokenCount(self,node):
        if self.IdtoIp[node.id] == node.ip_addr:
            self.tokenCount[node.id] += 1;
            