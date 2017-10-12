#!/usr/bin/python3

class Othello:
    def __init__(self, squares):
        self.player = 1
        self.squares = squares
        self.board = [['.' for i in range(squares)] for j in range(squares)]
        """self.board[(squares//2)-1][(squares//2)-1] = 'x'
        self.board[(squares//2)][(squares//2)-1] = 'o'
        self.board[(squares//2)-1][squares//2] = 'o'
        self.board[squares//2][squares//2] = 'x'"""
        self.board[2][2] = 'x'
        self.board[2][3] = 'x'
        self.board[2][4] = 'x'
        self.board[3][2] = 'x'
        self.board[4][2] = 'x'
        self.board[3][4] = 'x'
        self.board[4][4] = 'x'
        self.board[4][3] = 'x'
        self.board[1][1] = 'o'
        self.board[1][2] = 'o'
        self.board[1][3] = 'o'
        self.board[1][4] = 'o'
        self.board[1][5] = 'o'



    def printBoard(self):
        for i in range(self.squares):
            for j in range(self.squares):
                print(self.board[j][i], end=' ')
            print("")


    def placePiece(self, posX, posY, player):
        if player == 1:
            self.board[posX][posY] = 'x'
            self.player = 2
        else:
            self.board[posX][posY] = 'o'
            self.player = 1


    def checkWest(self, posX, posY, player, check):
        if (posX < 0):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkWest(posX-1, posY, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkWest(posX-1, posY, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return (True, (posX,posY))
                else:
                    return False

    def flipWest(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipWest(posX-1, posY, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipWest(posX-1, posY, player)


    def checkEast(self, posX, posY, player, check):
        if (posX > self.squares-1):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkEast(posX+1, posY, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkEast(posX+1, posY, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipEast(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipEast(posX+1, posY, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipEast(posX+1, posY, player)


    def checkSouth(self, posX, posY, player, check):
        if (posY > self.squares-1):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkSouth(posX, posY+1, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkSouth(posX, posY+1, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipSouth(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipSouth(posX, posY+1, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipSouth(posX, posY+1, player)


    def checkNorth(self, posX, posY, player, check):
        print("posY",posY)
        if (posY < 0):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkNorth(posX, posY-1, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkNorth(posX, posY-1, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipNorth(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipNorth(posX, posY-1, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipNorth(posX, posY-1, player)

    def checkNorthWest(self, posX, posY, player, check):
        if (posX < 0 or posY < 0):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkNorthWest(posX-1, posY-1, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkNorthWest(posX-1, posY-1, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipNorthWest(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipNorthWest(posX-1, posY-1, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipNorthWest(posX-1, posY-1, player)


    def checkNorthEast(self, posX, posY, player, check):
        if (posX > self.squares-1 or posY < 0):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkNorthEast(posX+1, posY-1, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkNorthEast(posX+1, posY-1, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipNorthEast(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipNorthEast(posX+1, posY-1, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipNorthEast(posX+1, posY-1, player)


    def checkSouthEast(self, posX, posY, player, check):
        if (posX > self.squares-1 or posY > self.squares-1):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkSouthEast(posX+1, posY+1, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkSouthEast(posX+1, posY+1, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipSouthEast(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipSouthEast(posX+1, posY+1, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipSouthEast(posX+1, posY+1, player)


    def checkSouthWest(self, posX, posY, player, check):
        if (posX < 0 or posY > self.squares-1):
            return False
        else:
            if (player == 1):
                if (self.board[posX][posY] == 'o'):
                    return self.checkSouthWest(posX-1, posY+1, player, True)
                elif (self.board[posX][posY] == 'x' and check == True):
                    return True
                else:
                    return False

            if (player == 2):
                if (self.board[posX][posY] == 'x'):
                    return self.checkSouthWest(posX-1, posY+1, player, True)
                elif (self.board[posX][posY] == 'o' and check == True):
                    return True
                else:
                    return False

    def flipSouthWest(self, posX, posY, player):
        if (player == 1):
            if (self.board[posX][posY] == 'o'):
                self.board[posX][posY] = 'x'
                self.flipSouthWest(posX-1, posY+1, player)
        if (player == 2):
            if (self.board[posX][posY] == 'x'):
                self.board[posX][posY] = 'o'
                self.flipSouthWest(posX-1, posY+1, player)


    def legalMove(self, posX, posY, player):
        if (self.board[posX][posY] == '.'):
            legal = False
            if(self.checkWest(posX-1, posY, player, False)):
                self.placePiece(posX, posY, player)
                self.flipWest(posX-1, posY, player)
                legal = True

            if (self.checkEast(posX+1, posY, player, False)):
                self.placePiece(posX, posY, player)
                self.flipEast(posX+1, posY, player)
                legal = True

            if (self.checkSouth(posX, posY+1, player, False)):
                self.placePiece(posX, posY, player)
                self.flipSouth(posX, posY+1, player)
                legal = True

            if (self.checkNorth(posX, posY-1, player, False)):
                self.placePiece(posX, posY, player)
                self.flipNorth(posX, posY-1, player)
                legal = True

            if (self.checkNorthWest(posX-1, posY-1, player, False)):
                self.placePiece(posX, posY, player)
                self.flipNorthWest(posX-1, posY-1, player)
                legal = True

            if (self.checkNorthEast(posX+1, posY-1, player, False)):
                self.placePiece(posX, posY, player)
                self.flipNorthEast(posX+1, posY-1, player)
                legal = True

            if (self.checkSouthEast(posX+1, posY+1, player, False)):
                self.placePiece(posX, posY, player)
                self.flipSouthEast(posX+1, posY+1, player)
                legal = True

            if (self.checkSouthWest(posX-1, posY+1, player, False)):
                self.placePiece(posX, posY, player)
                self.flipSouthWest(posX-1, posY+1, player)
                legal = True
            return legal
        else:
            return False


    def displayMoves(self, player):
        cordinatesOfMoves = []
        for i in range(self.squares):
            for j in range(self.squares):
                #1,3 valid move
                if (self.board[i][j] == '.'):
                    if (self.checkWest(i-1,j,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkEast(i+1,j,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkSouth(i,j+1,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkNorth(i,j-1,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkNorthWest(i-1,j-1,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkNorthEast(i+1,j-1,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkSouthWest(i+1,j+1,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkSouthEast(i-1,j+1,player,False)):
                        cordinatesOfMoves.append((i,j))





        return cordinatesOfMoves


    def game(self):
        winner = False
        tie = False
        while not(winner or tie):
            self.printBoard()
            pos = input(("Player {}, place your tile: ").format(self.player))
            if (pos == 'n'):
                listOfMoves = self.displayMoves(self.player)
                print(listOfMoves)
            elif (pos == "help"):
                print("type n to know your available moves or k if you don't have a move.")
            elif (pos == 'k'):
                listOfMoves = self.displayMoves(self.player)
                if (listOfMoves == []):
                    if (self.player == 1):
                        self.player = 2
                    else:
                        self.player = 1
                else:
                    print("There are available moves, please chose one.")
            elif (pos != 'n' and pos != "help"):
                try:
                    pos = pos.split(",")
                    if (self.legalMove(int(pos[0]), int(pos[1]), self.player)):
                        print("player",self.player)
                except ValueError:
                    print("Write your cordinates in the form of 'x,y'.")







myGame = Othello(8)
myGame.game()
