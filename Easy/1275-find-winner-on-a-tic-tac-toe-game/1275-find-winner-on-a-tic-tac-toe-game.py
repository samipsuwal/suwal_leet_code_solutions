class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def checkDiagonal(pMoves):
            return ([0,0] in pMoves and [1,1] in pMoves and [2,2] in pMoves) or ([0,2] in pMoves and [1,1] in pMoves and [2,0] in pMoves)

        def checkIfWon(x, y, moves):
            if checkDiagonal(moves):
                return True
            
            #check horizontal
            if 0 in x and x[0]==3:
                return True
            
            if 1 in x and x[1]==3:
                return True
            
            if 2 in x and x[2]==3:
                return True
            
            if 0 in y and y[0]==3:
                return True
            
            if 1 in y and y[1]==3:
                return True
            
            if 2 in y and y[2]==3:
                return True
            
            return False

        aMoves = []
        bMoves =[]
        aX={}
        aY={}
        bX={}
        bY={}
        switch = 1
        for move in moves:
            if switch ==1:
                switch *=-1

                aMoves.append(move)
                if move[0] not in aX:
                    aX[move[0]] = 1
                else:
                    aX[move[0]] +=1

                if move[1] not in aY:
                    aY[move[1]] = 1
                else:
                    aY[move[1]] +=1
                    
                if checkIfWon(aX, aY, aMoves):
                    return "A"
            else:
                switch *=-1
                bMoves.append(move)

                if move[0] not in bX:
                    bX[move[0]] = 1
                else:
                    bX[move[0]] +=1


                if move[1] not in bY:
                    bY[move[1]] = 1
                else:
                    bY[move[1]] +=1
                    
                if checkIfWon(bX, bY, bMoves):
                    return "B"

        print(aMoves)       
        
        print(bMoves)
        
        

        if len(moves) <9:
            return "Pending"
        return "Draw"
        