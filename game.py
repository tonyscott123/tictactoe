# +++ Tic Tac Doe console game +++
# @author: TScott


# how to run: paste the code below into any python ide, eg:
#  https://www.programiz.com/python-programming/online-compiler/

import random
import time

board = [[1,2,3],[4,5,6], [7,8,9]]
players = {
    1: {"type": "human",    "symb" :"X"}, 
    2: {"type": "computer", "symb": "0"}
    }
max_moves = sum([len(row) for row in board])


def show_board():
    ''' displays the board in grid format '''
    
    # convert all values to str to maintain board size
    str_board = [[str(x) for x in row] for row in board]
    
    # display the board as grid
    for i in str_board:
        print(str(i), sep ="")
        
        
def trigger_random_move(player):
    ''' selects a tile  from the board at random '''
    
    # filter for int values as to remove player symbols
    stripped_rows_v1 = [[val for val in row if type(val) == int] 
    for row in board]
    
    # strip any empty rows []
    stripped_rows_v2 =[row for row in stripped_rows_v1 if row]
    
    # randomly select from available tiles
    random_move = random.choice(
        random.choice(stripped_rows_v2)
        )
    return random_move
    
def validate_selection():
    pass
    

def process_move(tile_num, player_symb):
    ''' finds/sets the player's symbol in the chosen tile  '''
       
    for i,x in enumerate(board):
       if tile_num in x:
           x[x.index(tile_num)]= player_symb
    show_board()
    return
           
    
def check_for_win(player):
    '''Create rows, diags, and cols and check for win '''

    rows = [x for x in board]
    # filter out int values and duplicate symbols 
    # return row win if size of list is 1 (symbol) 
    if [set(x) for x in rows if len(set(x)) ==1]:
        print("{} won by row".format(player["type"]))
        return (player, "row_win")
    
    cols = [list(col) for col in zip(*rows)]
    # return col win if size of list is 1 (symbol) 
    if [set(x) for x in cols if len(set(x))==1]:
        print("{} won by col".format(player["type"]))
        return (player, "col_win")
    
    diags = "test"
    # return (player,"no_win")
    return (player, "no_win")
    
def toggle_turns(max_moves, player = players[1]):
    ''' recursively toggles play turns across players
        and manage processes each play
    '''
    
    if player is players[1]:
        avail_tiles=[val for row in board for val in row if type(val)==int]
        while True:
            try:
                tile_selected = int(input('Select any available numbered tile [1-9] | You selected: '))
                if tile_selected in avail_tiles:
                    break
                else:
                    print(" Tile already selected. Please select from available numbered tiles: {}".format(avail_tiles))
            except ValueError:
                print("Invalid input. Please enter a number.")
                
            
    if player is players[2]:
        tile_selected = trigger_random_move(player["symb"])
        print("Computer's turn| Computer selected: {}".format(tile_selected))
        
    process_move(tile_selected, player["symb"])
    max_moves -=1
    result = check_for_win(player) 
    
    if result[1]!= "no_win":
        return result
    if max_moves ==0:   
        return "max_moves reached. No Wins!"
        
    player = players[1] if player == players[2] else players[2]
    toggle_turns(max_moves, player)
    
         
def start_game():
    print("""+++ Welcome to the Tic Tac Doe console game +++ \n
=========
This game comprises 2 players and consists in selecting tiles 
on the board (shown below).
Each player, assigned a symbol (nought("O") or cross("X")),
turn by turn, selects any available numbered tile on the board 
The aim is to the assigned symbol across a full row, column, 
or diagonal, before the other player does.
""")

    show_board()
    print("""
Example:
    - A win by player with symbol "X" could be across any row (or column diag):
   row: [1,2,3] --> ["X","X","X"]
    - A win by player with symbol "O" could be across any colum (or row, diag): 
    column: [2,5,8] --> ["O","O","O"]
[Note]: a game can have no wins where no symbol were attained across rows, cols, or diagonals by any player
 ==========
   
Ready to Start the Game?
You are assigned Player 1 with symbol ("X") playing against 
the computer Player 2, assigned the symbol("O"). 
-- Human VS Machine - Who Will Win?!!! --- 

[√] Remember to always scroll down the during game with the down arrow key
""")

    show_board()
    print(toggle_turns(max_moves))
    
    
#Call Game
start_game()
    
    
    
    

    
