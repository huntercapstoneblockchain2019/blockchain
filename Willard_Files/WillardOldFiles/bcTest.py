import Block
import BChain
import time

def main():
    blockChain = []

    # Creation of The Genesis Block
    GenesisBlock = Block.Block(
        '0', ('Aiza Khan', 'Jamie Fernandez', 'Jessica Gutierrez', 'Willard Joseph'))

    # Adding the Genesis Block to the Block Chain List
    blockChain.append(GenesisBlock)

    # Checking the First Block's Information
    (blockChain[0].retriveBlockInfo())

    # Creation of Second Block
    SecondBlock = Block.Block(blockChain[0].getBlockHash(), ('Team BlockChain Received an A for Capstone'))

    # Adding Second Block to the Chain
    blockChain.append(SecondBlock)

    # Checking the Second Block's Information
    (blockChain[1].retriveBlockInfo())

    # Creation of Third Block
    ThirdBlock = Block.Block(blockChain[1].getBlockHash(), ('Team Blockchain has created a multi-billion dollar platform'))

    # *** ABOVE CODE WAS USED TO TEST THE BLOCK METHODS ***

    # Creation of Block Chain
    testBlockChain = BChain.BlockChain()

    # Getting the Number of Blocks Currently in Chain
    # Assertion: Should be 0
    print('Current Block Count:', testBlockChain.getBlockCount())
    assert testBlockChain.getBlockCount() == 0

    # Testing Validity Function
    # Test#1: Should be True as there are 0 Blocks
    print('Validity Test #1', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == True

    # Adding the GenesisBlock to the Block Chain
    testBlockChain.addBlock(GenesisBlock)

    # Testing Validity Function
    # Test#2: Should be True as there is 1 Block and the Block's previousHash is 0
    print('Validity Test #2', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == True

    # ***Important Note This Method Will Be Removed as a BlockChain is immutable. Testing Purposes Only ***
    testBlockChain.deleteAllBlocks()

    # Testing Validity Function
    # Test#3: Should be False as there is 1 Block and the Block's previousHash is not 0
    testBlockChain.addBlock(SecondBlock)
    print('Validity Test #3', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == False
   
    # Testing Validity Function
    # Test#4: Should be True as there are 2 Blocks and the appropriate hashes match
    testBlockChain.deleteAllBlocks()
    testBlockChain.addBlock(GenesisBlock)
    testBlockChain.addBlock(SecondBlock)
    print('Validity Test #4', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == True

    # Testing Validity Function
    # Test#5: Should be False as there are 2 Blocks whose hashes don't match
    testBlockChain.deleteAllBlocks()
    testBlockChain.addBlock(GenesisBlock)
    testBlockChain.addBlock(GenesisBlock)
    print('Validity Test #5', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == False
    
    # Testing Validity Function
    # Test#6: Should be True as there are 3 Blocks whose hashes match properly
    testBlockChain.deleteAllBlocks()
    testBlockChain.addBlock(GenesisBlock)
    testBlockChain.addBlock(SecondBlock)
    testBlockChain.addBlock(ThirdBlock)
    print('Validity Test #6', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == True

    # Testing Validity Function
    # Test#7: Should be False as there are 3 Blocks whose hashes don't match properly
    testBlockChain.deleteAllBlocks()
    testBlockChain.addBlock(GenesisBlock)
    testBlockChain.addBlock(ThirdBlock)
    testBlockChain.addBlock(SecondBlock)
    print('Validity Test #7', testBlockChain.getChainValidity())
    assert testBlockChain.getChainValidity() == False

    # Printing Out the Block Chain
    # testBlockChain.printChainInfo()

    # Testing of the AddValidBlock() 
    testBlockChain2 = BChain.BlockChain()
    
    # Testing AddValidBlock
    # Test#1: Should not allow Block to be added as the Block doesn't have a PreviousHash of 0
    print('Test#1 :')
    testBlockChain2.addValidBlock(ThirdBlock)
    # Nothing was added so the count should be 0
    assert testBlockChain2.getBlockCount() == 0

    # Testing AddValidBlock
    # Test#2: Should allow the Genesis Block to Be added.
    print('Test#2 :')
    testBlockChain2.addValidBlock(GenesisBlock)
    # Genesis Block was added so the count should be 1
    assert testBlockChain2.getBlockCount() == 1

    #Testing AddValidBlock
    #Test #3: Should Deny Access to a Block that doesn't match the last Valid Block's Hash code
    print('Test#3 :')
    testBlockChain2.addValidBlock(ThirdBlock)
    # This Block was denied count remains 1
    assert testBlockChain2.getBlockCount() == 1

    #Testing AddValidBlock
    #Test #4: Block should be accepted as it is a legitimate Block and their hashes align
    print('Test#4 :')
    testBlockChain2.addValidBlock(SecondBlock)
    # This Block was accepted count increases to 2
    assert testBlockChain2.getBlockCount() == 2

    # Testing AddValidBlock
    # Test #5: Should Deny Access as the entire Chain will be invalid. I will utilize the old addBlock function which has no
    # validation to enter an invalid Block, then try and add a Block utilizing addValidBlock()
    print('Test#5 :')
    # Block illegally added to Chain
    testBlockChain2.addBlock(SecondBlock)
    testBlockChain2.addValidBlock(ThirdBlock)
    # This Block was denied count increases to 3 because of the illegally added Block. However, doesn't increase to 4 because
    # the chain is invalid
    assert testBlockChain2.getBlockCount() == 3
    assert testBlockChain2.getChainValidity() == False

    # Retrieval of the last 2 Blocks to show that this is an invalid Chain
    testBlockChain2.printSpecifiedChainInfo(2)

    
    print(time.time())


main()
