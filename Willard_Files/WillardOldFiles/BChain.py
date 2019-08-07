import Block

class BlockChain:
    'Class for The BlockChains backbone: a wrapper around a Python List'

    '''
    In the interim the Basic Data Structure will be based upon a Python List
    # TODO: Add the feature to check if the Block Chain is valid - ***COMPLETED***
    # TODO: Add the feature to add a new Block - ***COMPLETED***
    Important to note that once a Block is added it can not be removed therefore we are not implementing any removal features
    in the final release of this application
    # TODO: Research if it is possible for any two blocks to have the same Hash Value
    '''

    # Constructor for the BlockChain's Backbone
    # TODO: Look into possibly changing this to a special type of linked list.
    def __init__(self):
        # Initial Values
        self.__theChain = []
        self.__blockCount = 0

    #TODO: Remove once addValidBlock Method is completed and fully tested. 
    # Can and will be used to create invalid Chains for testing purposes
    # This Method will be deprecated for addValidBlock()
    def addBlock(self, Block):
        self.__theChain.append(Block)

    # Prints the Content of the entire Chain
    def printChainInfo(self):
        for b in self.__theChain:
            (b.retriveBlockInfo())
    
    # Prints the n last Blocks 
    def printSpecifiedChainInfo(self, N):
        if N > self.getBlockCount():
            print('There are not enough Blocks to be printed')
        elif N == self.getBlockCount():
            self.printChainInfo()
        elif N == 0 :
            print('Why call me then...?')
        else:
            i = self.getBlockCount() - N
            while i < self.getBlockCount():
                self.__theChain[i].retriveBlockInfo()
                i += 1

    # TODO: Remove this function.
    def deleteAllBlocks(self):
        self.__theChain.clear()

    # Returns the count of the amount of valid Blocks in Chain
    def getBlockCount(self):
        return len(self.__theChain)

    
    # Returns True for a Valid Chain and False for a Chain that doesn't meet the specifications.
    def getChainValidity(self):
        # TODO: TEAM PLEASE THINK ABOUT ANY CONDITIONS THAT I MAY NOT HAVE THOUGHT ABOUT
        # Condition 1: if getBlockCount() = 0, then chain is Valid
        # Condition 2: if getBlockCount() = 1, then block on the chain must have a prevHash of 0
        #              this condition will be enforced by the addBlock method.
        # Condition 3: if getBlockCount() >1, then chain is valid if Block[i] prevHash is == to
        #              Block[i-1] blockHash
        if self.getBlockCount() == 0:
            return True
        elif self.getBlockCount() == 1 and self.__theChain[0].getPreviousHash() == '0':
            return True
        elif self.getBlockCount() > 1:
            i = 1
            while i < self.getBlockCount():
                if self.__theChain[i].getPreviousHash() != self.__theChain[i-1].getBlockHash():
                    return False

                i += 1
            return True
        else:
            return False

    def addValidBlock(self, Block):
        # TODO: TEAM PLEASE THINK ABOUT ANY CONDITIONS THAT I MAY NOT HAVE THOUGHT ABOUT
        # Condition #1: Valid Chain and Empty Chain (This is verbose as an empty chain will always be valid)
        #              We must now check that the Block trying to be added has a previousHash value of 0 
        #              if these conditions aren't met, Block will be denied entry into chain.
        # Condtion #2: Valid Chain which means all blocks have been properly verified and that their hashes align
        #              correctly. It is important to now verify that the Block being added has the proper hash value
        #              lastBlockInChain.getBlockHash() == potentialBlockToBeAdded.previousHash(). This condition may
        #              help solve and validate the Proof of Work Step if it needs to be implemented.
        # Condition #3: No Blocks will ever be accepted by a invalid Chain. Therefore, until the error is corrected this
        #               chain will allow no other activity to be completed
        if self.getChainValidity() == True and self.getBlockCount() == 0:
            if Block.getPreviousHash() == '0':
                self.__theChain.append(Block)
                print('Block Added to Valid Chain.')
            else:
                print('Genesis block must have Previous Hash of 0. Block Not added')
        elif self.getChainValidity() == True and self.getBlockCount() > 0:
            if self.__theChain[self.getBlockCount() - 1].getBlockHash() == Block.getPreviousHash():
                self.__theChain.append(Block)
                print('Block Added to Valid Chain.')
            else:
                print('Invalid Block prohibited from being added to chain. Rework your PoW')
        else:
            print('Block was not added. This BlockChain is corrupted.')
