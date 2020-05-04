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
        print("Actions permises :", game.Allowedactions())
        Affichage(game.board)
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
                    print("vous jouez", move)
                    if human == 'X':
                        game.board[move] = 1
                    if human == 'O':
                        game.board[move] = -1
                    turn = 'bot'
        elif turn == 'bot' and game.isGameover() == False:
            move = bot.action(game)            
            print("the computer plays", move)
            if human == 'X':
                game.board[move] = -1
            if human == 'O':
                game.board[move] = 1
            turn = 'human'
    if game.isPositivewinner() == True:
        print("Player X wins")
        Affichage(game.board)
    elif game.isNegativewinner() == True:
        print("Player O wins")
        Affichage(game.board)
    elif game.Allowedactions() == []:
        print("Draw")
        Affichage(game.board)
    game.Reset()
            
                
            
            
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
    board_neutral =   " {} ¦ {} ¦ {} \n" + \
                "---+---+--- \n" + \
               " {} ¦ {} ¦ {} \n" + \
                "---+---+--- \n" + \
               " {} ¦ {} ¦ {} \n"
    board_letters = Numtoletters(board)
    print(board_neutral.format(*board_letters))
    
    


class RandomBot:
    def __init__(self):
        """ Returns a random move given game """
        
    def action(self, game):
        return random.choice(game.Allowedactions())





partie_test = Game()             # Création d'une partie test
partie_classique = Game()        # Création d'une partie classique



board_test = [0, 0, 0,
              0, -1, 0,
              1, 0, 0]


board_classique = [0, 0, 0,
                   0, 0, 0,
                   0, 0, 0]

# partie_test.board = board_test
partie_classique.board = board_classique


# play(partie_test)
play(partie_classique)





