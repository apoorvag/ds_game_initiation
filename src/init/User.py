'''
Created on Mar 31, 2013

@author: apoorva
'''
import RequestMessage
import random
import cards
import socket


#input: Deck of cards and number of cards that need to be chosen
#output: Chosen cards and remaining deck of cards
def select_cards(self,DECK,numberOfCards):
        #generate required number of hands    
        hand = random.sample(DECK, numberOfCards)
        for card in hand:
            DECK.remove(card)
        #return the cards selected and the remaining cards in deck
        return (hand,DECK,numberOfCards)
    
#obtains the IP address of the host. Can change code depending on further updates
def getMyIP():
    print "needs code here which returns ipaddress"
    return(socket.gethostbyname(socket.gethostname())) 

#input: list of objects of type NodeIdentity sorted by the value of their ids
def findMyNodes(nodeIdList):
    #Finds the node corresponding to the current host calling this function
    for node in nodeIdList:
        if node.ip_addr == getMyIP():
            myNode = node
            break
        #finds the index of this node in the list
        curIndex = nodeIdList.index(myNode)
        #if curIndex-1 value exists, it becomes the predecessor
        if curIndex-1 >= 0:
            predIndex = curIndex -1
        else: 
        #for element with the smallest index, last element becomes the predecessor
            predIndex = len(nodeIdList)-1; 

        if curIndex +1 < len(nodeIdList):    
            succIndex = curIndex + 1
        else:
        #for the element with the largest index first element becomes the successor
            succIndex = 0
        
        predNode = nodeIdList.index(predIndex)
        succNode = nodeIdList.index(succIndex)
        return myNode, predNode, succNode
    
def sendMsg(ipAddr , RequestMessage):
    print"this is send message in User module"
    
def receiveMsg(ip_addr , msg):
    s_port = d_port = ts = 0 
    myNode , predNode, succNode = None
    if msg.type == "NODELIST":
        myNode , predNode, succNode  = findMyNodes(msg.data)
        #creating 3 separate buffers
        myBuffer = cards.cardBuffer(myNode)
        predBuffer = cards.cardBuffer(predNode)
        succBuffer = cards.cardBuffer(succNode)
        ACK = RequestMessage(getMyIP,ip_addr,s_port,d_port,"ACK",ts,"")
        sendMsg(ip_addr, ACK)
    elif msg.type == "TOKEN":
        data = msg.data
        tok = data.getToken()
        if tok.checkValid(myNode.id) == False:
            print "Did not go through all nodes. Needs to wait"
        else:
            (hand, DECK, number) = select_cards(data.cards , data.noOfCards)
        tok.tokenId = succNode.id
        tc = cards.token_cards()
        tc.token = tok;
        tc.cards = DECK
        tc.noOfCards = number
        fwdMsg = RequestMessage(myNode.ip_addr,succNode.ip_addr,myNode.port,succNode.port,"TOKEN",ts,tc)
        sendMsg(succNode.ip_addr, fwdMsg)
        print "implement a termination condition for ending the token "