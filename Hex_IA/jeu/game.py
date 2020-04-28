import numpy as np

class Game:
    def __init__(self):
        self.name = "Tic-tac-toe"
        self.board = [0,0,0,0,0,0,0,0,0]
        #self.currentplayer = 1      # First to play is 1, second is -1
        self.currentplayer = "cross"      # First to play is cross, second is circle


    def allowedActions(self):
        allowed = []
        for i in range(len(self.board)):
            if self.board[i] == 0:
                allowed.append(i)

        return allowed

    def winningPositions(self):
        winningPositions = [[0,1,2],[3,4,5],[6,7,8],
                           [0,3,6],[1,4,7],[2,5,8],
                           [0,4,8],[2,4,6]]
        for vect in winningPositions:     # [3,4,5]
            s = self.board(vect[0]) + self.board(vect[1]) + self.board(vect[2])
            if s == 3:
                winner = player1
            elif s == -3:
                winner = player2





    def _player1Win(self):
        win1 = False
        if

    def _isgameOver(self):
        if self.board = []

    def _reset(self):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.currentplayer = 1



partie1 = Game()   # Création d'une nouvelle partie

board1 = [0, 0, 1,
          1, 0, 2,
          1, 0, 2]
partie1.board = board1
partie1.board
partie1.allowedActions()







def actions_permises(board):
    allowed = []
    for i in range(len(board)):
        if board[i] == 0:
            allowed.append(i)

    return allowed



bbb = actions_permises(board1)




class Game:

    def __init__(self):
        self.gameState =