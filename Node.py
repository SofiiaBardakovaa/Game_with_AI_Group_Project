class Node:
    def __init__(self, move,depth,currentNumber, personScore, computerScore, bank, turn): 
        self.children = []
        self.depth = depth
        self.currentNumber = currentNumber
        self.personScore = personScore
        self.computerScore = computerScore
        self.bank = bank 
        self.turn = turn # 1 for player, 0 for computer
        self.move = move # 2 or 3 or 4



    def generateChildNodes(self):
        if self.currentNumber <= 10:
            return
        
        for i in [2,3,4]:
            newNumber = self.currentNumber // i
            newPersonScore = self.personScore
            newComputerScore = self.computerScore
            newTurn = self.turn
            newBank = self.bank
            if(newNumber % 2 == 0 and self.turn == 1):
                newPersonScore -= 1
            elif(newNumber % 2 != 0 and self.turn == 1):
                newPersonScore += 1
            elif(newNumber % 2 == 0 and self.turn == 0):
                newComputerScore -= 1
            elif(newNumber % 2 != 0 and self.turn == 0):
                newComputerScore += 1
            if(newNumber % 5 == 0):
                newBank += 1


            if self.turn == 1:
                newTurn = 0
            else:
                newTurn = 1


            childNode = Node(i,self.depth+1,newNumber,newPersonScore,newComputerScore,newBank,newTurn)
            self.children.append(childNode)



            


