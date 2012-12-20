#   http://blockchain.info/api/api_send

import webbrowser
import urllib2
import codecs
import string
import json
import os

class SendManyTransactions:
    response = {}
    privateKey = ""
    totalShares = 0
    recipients = ""
    batchObject = ""
    totalBitcoins = .0
    bitcoinsPerShare = .0
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        
    def createNewBatch(self, batchName):
        batchDirPath = os.path.dirname(os.path.abspath(__file__)) + '\\batches\\'
        
        if not os.path.exists(batchDirPath):
            os.makedirs(batchDirPath)
                
        if os.path.exists(batchDirPath + batchName + '.txt'):
            return  # "Batch Transaction File already exists"
                
        writeObject = codecs.open(batchDirPath + batchName + '.txt','w')
        writeObject.write('1JzSZFs2DQke2B3S4pBxaNaMzzVZaG4Cqh:2\n12Cf6nCcRtKERh9cQm3Z29c9MWvQuFSxvT:5\n1dice6YgEVBf88erBFra9BHf6ZMoyvG88:7')
        writeObject.close()
        
        webbrowser.open(batchDirPath + batchName + '.txt')
        
    def loadBatch(self, batchName):
        batchDirPath = os.path.dirname(os.path.abspath(__file__)) + '\\batches\\'

        readObject = open(batchDirPath + batchName + '.txt','r')
        self.batchObject = readObject.read()
        readObject.close()
        
    def prepareBatch(self):
        assetHolders = self.batchObject.split('\n')
        
        self.recipients = '{'
        
        self.totalShares = 0
        self.totalBitcoins = .0
        
        for assetHolder in assetHolders:
            address, numberOfShares = assetHolder.split(":")
            div = self.bitcoinsPerShare * float( numberOfShares )
            self.totalBitcoins = self.totalBitcoins + div
            self.recipients = self.recipients + '"' + address + '":' + str( "%.8f" % div ).replace(".", "") + ','
            self.totalShares = self.totalShares + int( numberOfShares )
            
        self.recipients = self.recipients[:self.recipients.__len__() - 1] + '}'
        
    def prepareParams(self, privateKey, bitcoinsPerShare):
        self.privateKey = privateKey
        self.bitcoinsPerShare = float( bitcoinsPerShare.strip() )

    def sendBatch(self):
        stringURL = "https://blockchain.info/merchant/{0}/sendmany?recipients=".format( self.privateKey )
        
        self.response = json.loads( urllib2.urlopen(stringURL + urllib2.quote( self.recipients )).read() )

        self.privateKey = ""

    def getResponse(self):
        return self.response
        
    def getTotalShares(self):
        return self.totalShares
    
    def getTotalBitcoins(self):
        return self.totalBitcoins
    
    def getBitcoinsPerShare(self):
        return self.bitcoinsPerShare