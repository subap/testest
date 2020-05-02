import numpy as np
import random

winningpositions = [[0,1,2],[3,4,5],[6,7,8],
                    [0,3,6],[1,4,7],[2,5,8],
                    [0,4,8],[2,4,6]]

class Game:
    def __init__(self):
        self.name = "Tic-tac-toe"
        self.board = [0,0,0,0,0,0,0,0,0]
        #self.currentplayer = 1      # First to play is 1, second is -1
        self.currentplayer = "cross"      # First to play is cross, second is circle
        self.legal_players = ["X","O"]
        

    def Reset(self):
        self.board = [0,0,0,0,0,0,0,0,0]    # Plateau par défaut
        self.currentplayer = 1
        
        
    def Allowedactions(self):
        allowed = []
        for i in range(len(self.board)):
            if self.board[i] == 0:
                allowed.append(i)
        return allowed
    
    
    def isPositivewinner(self):
        positivewinner = False
        for vect in winningpositions:     # [3,4,5]
            s = self.board[vect[0]] + self.board[vect[1]] + self.board[vect[2]]
            if s == 3:
                positivewinner = True
        return positivewinner
     
    def isNegativewinner(self):
        negativewinner = False
        for vect in winningpositions:
            s = self.board[vect[0]] + self.board[vect[1]] + self.board[vect[2]]
            if s == -3:
                negativewinner = True
        return negativewinner
            
    
    def isGameover(self):
        gameover = False
        if self.Allowedactions() == [] or self.isPositivewinner() == True or self.isNegativewinner() == True:
            gameover = True
        return gameover

    def nbPlayedmoves(self):
        return 9 - len(self.Allowedactions())


    def Playerturn(self):
        playerturn = None
        if self.nbPlayedmoves() % 2 == 0:
            playerturn = "cross"
        else:
            playerturn = "circle"
        return playerturn



def play(game):
    human = None
    bot = RandomBot()
    while human is None:
        human = input("Select player: {} (cross begins)".format(game.legal_players)).upper()
        if human not in game.legal_players:
            print("Invalid option")
            human = None
    turn = None
    if human == 'X' and game.Playerturn() == "cross" or human == 'O' and game.Playerturn() == "circle":
        turn = 'human'
    else:
        turn = 'bot'
    while game.isGameover() == False:
        if turn == "human":
            move = None
            while move == None:
                move = input("human, please play")
                if move.upper()[:1] == "Q":
                    print("you quit the game")
                    return
                if move.isdigit():
                    move = int(move)
                if move in game.Allowedactions():
                    print("vous jouez")
            turn = 'bot'
        else:       # if turn = 'bot'
            print("the computer plays")
            move = bot.action(game)
            turn = 'human'
                
            
            
def Numtoletters(board):
    letters = []
    for i in board:
        if i == 0:
            letters.append(' ')
        if i == 1:
            letters.append('X')
        if i == -1:
            letters.append('O')
    return letters

            
def Affichage(board):
    jijiji =   " {} ¦ {} ¦ {} \n" + \
                "---+---+--- \n" + \
               " {} ¦ {} ¦ {} \n" + \
                "---+---+--- \n" + \
               " {} ¦ {} ¦ {} \n"
    board_letters = [i for i in Numtoletters(board)]
    print(jijiji.format(*board_letters))
    
    


class RandomBot:
    def __init__(self):
        """ Returns a random move given game and player """
        self.memo = {}
        
    def action(self, game):
        return random.choice(game.Allowedactions())



print("J'ai {} ans".format(18))
print("J'ai {} ans et {} mois".format(18, "trois"))



partie_test = Game()        # Création d'une nouvelle partie
partie_test_bis = Game()    # Création d'une nouvelle partie


board_test = [0, 0, 1,
              1, 0, -1,
              1, 0, -1]
board_test_bis = [1, 0, 1,
                  1, -1, -1,
                  1, 0, -1]
partie_test.board = board_test
partie_test_bis.board = board_test_bis

partie_test.Playerturn()

play(partie_test)




bottest = RandomBot()
bottest.action(partie_test)

Affichage(partie_test)



