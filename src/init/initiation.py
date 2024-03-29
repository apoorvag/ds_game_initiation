'''
Created on Mar 29, 2013

@author: apoorva
'''
from random import random
from random import randint
import operator
import RequestMessage
import time
import token
import cards
import NodeIdentity
    
Initiator = True

#Input: List of nodes of type NodeIdentity
#Output: List of nodes with respective nodeIds generated 
def genId(nodeIdList):
    collisionCheck = []
    #generation of ids is the privilege of the initiator only
    if(Initiator == True):
        #generate rand id for every node in nodelist    
        for node in nodeIdList: 
            random.seed([node.ip_addr]) 
            node.id = randint(9,10000000)
            #if the random number has already been generated
            while node.id in collisionCheck:
                node.id = randint(1000,10000000) 
            #append the newly generated unique id to the list     
            collisionCheck.append(node.id)
            
    return nodeIdList

#definitions needs to be replaced by code for sending the message
def sendMsg(ipAddr , RequestMessage):
    print"this is send message"

#time out period 20s waiting for acknowledgments   
def waitForAck():
    time.sleep(20)

#check if the id has a corresponding acknowledgment from the list    
def findRelevantNode(Id , AckList):
    for node in AckList:
        if node.id == Id:
            if node.type == "ACK": #has to respond with true only for ACK
                return True
            
#generate the token that is going to be passed around
def genToken(nlist):
    ipTOid =[]
    for node in nlist:
        ipTOid[node.id]= node.ip_addr
    return(token(ipTOid,nlist))
        
         
#generate the token and send it to the node with smallest id
def StartInitiation(node, nodeList):
    getIp = 0
    dest = 0
    s_port = 0
    d_port = 0
    ts = 0
    #generating the relevant token
    tok = genToken(nodeList)
    obj = cards.cards_init(nodeList)
    cardSet = obj.gen_cards() 
    tc = cards.token_cards()
    tc.token = tok;
    tc.cards = cardSet;
    tc.noOfCards = obj.eachPlayerCards
    destNode = nodeList[0]
    tok.id = destNode.id
    #generating the initialization message with token and deck of cards as the data
    init = RequestMessage(getIp,destNode.ip_addr,s_port,destNode.port,"TOKEN",ts,tc)
    #send the token message to the lowest id node
    sendMsg(node.ip_addr,init)

            
#input: List of nodes
#function sends and confirms all nodes a list of ids
def sendId(nodeIdList):
        AckList = []
        unAckList = []
        deadNode = []
        nodeIdList.sort(key = operator.attrgetter('id'))
        getIp = 0
        dest = 0
        s_port = 0
        d_port = 0
        ts = 0
        msg = RequestMessage(getIp,dest,s_port,d_port,"NODELIST",ts,nodeIdList)
        for node in nodeIdList:
            sendMsg(node.ip_addr, msg) 
        waitForAck()    
        #At this point check to see if all acknowledgments have been received
        #Add unacknowledged nodes into another list
        for node in nodeIdList:
            if findRelevantNode(node.id,AckList) != True:
                unAckList.append(node)
        waitForAck()
        for node in unAckList:
            if findRelevantNode(node.id,AckList) != True:
                deadNode.append(node)        
        if len(deadNode) == 0:
            print "All nodes have acknowledged"
            StartInitiation(nodeIdList.pop(), nodeIdList) 
        else:
            print "All nodes have not been acknowledged" 