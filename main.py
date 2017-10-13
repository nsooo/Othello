#!/usr/bin/python3

class Othello:
    def __init__(self, squares):
        if (squares % 2 != 0 or squares < 4):
            self.squares = squares
        else:
            self.player = 1
            self.squares = squares
            self.board = [['.' for i in range(squares)] for j in range(squares)]
            self.board[(squares//2)-1][(squares//2)-1] = 'x'
            self.board[(squares//2)][(squares//2)-1] = 'o'
            self.board[(squares//2)-1][squares//2] = 'o'
            self.board[squares//2][squares//2] = 'x'

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
                    if (self.checkSouthWest(i-1,j+1,player,False)):
                        cordinatesOfMoves.append((i,j))
                    if (self.checkSouthEast(i+1,j+1,player,False)):
                        cordinatesOfMoves.append((i,j))
        return list(set(cordinatesOfMoves))


    def checkWinner(self):
        player1Moves = []
        player1Moves = self.displayMoves(1)
        player2Moves = []
        player2Moves = self.displayMoves(2)
        if (player1Moves == [] and player2Moves == []):
            return True
        else:
            return False

    def countBoard(self):
        player1 = 0
        player2 = 0
        for i in range(self.squares):
            for j in range(self.squares):
                if (self.board[i][j] == 'x'):
                    player1 += 1
                elif (self.board[i][j] == 'o'):
                    player2 += 1
        return player1, player2


    def game(self):
        if (self.squares % 2 != 0 or self.squares < 4):
            print("The board must have an even integer and minimum a 4.")
        else:
            print("Type '?' to get available commands.")
            winner = False
            while not(winner):
                self.printBoard()
                pos = input(("Player {}, place your tile: ").format(self.player))
                if (pos == 'n'):
                    listOfMoves = self.displayMoves(self.player)
                    print(listOfMoves)
                elif (pos == "?"):
                    print("type n to get a list of your possible moves or k if you don't have any moves.")
                elif (pos == 'k'):
                    listOfMoves = self.displayMoves(self.player)
                    if (listOfMoves == []):
                        print("Changed player turn.")
                        if (self.player == 1):
                            self.player = 2
                        else:
                            self.player = 1
                    else:
                        print("There are available move(s), please choose one.")
                else:
                    try:
                        pos = pos.split(",")
                    except ValueError:
                        print("Write your cordinates in the form of 'x,y'.")

                    else:
                        if (self.legalMove(int(pos[0]), int(pos[1]), self.player)):
                            winner = self.checkWinner()
            self.printBoard()
            player1, player2 = self.countBoard()
            if (player1 > player2):
                print("Player 1 is the winner with", player1, "to", player2, "tiles!")
            elif (player1 < player2):
                print("Player 2 is the winner with", player2, "to", player1, "tiles!")
            else:
                print("It's a tie!")


try:
    number = int(input("How big should the board be, n x n: "))
except ValueError:
    print("The board size must be an integer.")
else:
    myGame = Othello(number)
    myGame.game()
