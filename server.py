# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template
from flask_session import Session
import random


# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 
# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/')
def index():
    board = [[None, None, None],[None, None, None],[None, None, None]]
    turn = "X"
    #player X plays first by default
    return render_template('index.html', game = board, turn=turn)



    
def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    if(board[0][0] == board[0][1] == board[0][2]):
        winner = board[0][0]
        # print(winner + (" first row"))
        
    elif(board[1][0] == board[1][1] == board[1][2]):
        winner = board[1][0]
        # print(winner + (" middle row"))

    elif(board[2][0] == board[2][1] == board[2][2]):
        winner = board[2][0]
        # print(winner + (" last row"))

    elif((board[0][0] == board[1][1] == board[2][2])):
        winner = board[0][0]
        # print(winner + (" left diagonal"))
        
    elif((board[2][0] == board[1][1] == board[0][2])):
        winner = board[2][0]
        # print(winner + (" right diagonal"))
    
    elif((board[0][0] == board[1][0] == board[2][0])):
        winner = board[0][0]
        # print(winner + (" first column"))
        
    elif((board[0][1] == board[1][1] == board[2][1])):
        winner = board[0][1]
        # print(winner + (" middle column"))
    
    elif((board[0][2] == board[1][2] == board[2][2])):
        winner = board[0][2]
        # print(winner + (" last column"))
    else:
        winner = None
        
    return winner


def other_player(player):
    """Given the character for a player, returns the other player."""
    assert player != None
    if player == 'X':
        return 'O'  # FIXME
    else:
        return 'X'

def bot_play(self, turn):
		board_x = random.randint(0,2)
		board_y = random.randint(0,2)

		if (self.board[board_x][board_y] != None):
			self.bot_play(self.turn)
		else:
			print('----> Bot chose index ', board_x, ', ', board_y)
			self.board[board_x][board_y] = 'O'



if __name__=='__main__':
    app.run(debug = True)