import random
import numpy as np
import math
import random
ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
EMPTY = 0
RED = 1
BLUE = 2
def evaluate_window(window, piece):
	score = EMPTY
	opp_piece = BLUE
	if piece == BLUE:
		opp_piece = RED
	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(0) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(0) == 2:
		score += 2
	if window.count(opp_piece) == 3 and window.count(0) == 1:
		score -= 4
	return score


def score_position(board, piece):
	score = 0
	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)
	return score

def get_next(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r
def drop(board, row, col, player):
    board[row][col] = player
       
def pick_best_move(board, piece):
	valid_locations = get_valid_locations(board)
	best_score = -math.inf
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next(board, col)
		temp_board = board.copy()
		drop(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col
	return best_col

def is_valid(board, col):
    return board[5][col] == 0
def get_valid_locations(board):
	valid_locations = []
	for col in range(7):
		if is_valid(board, col):
			valid_locations.append(col)
	return valid_locations

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True
def is_terminal(board):
    return winning_move(board , 1 ) or winning_move(board , 2) or len(get_valid_locations(board)) == 0
def minimax(board, depth, player):
    valid_location = get_valid_locations(board)
    terminal = is_terminal(board)
    if depth == 0 or terminal:
        if terminal:
            if winning_move(board,1):
                return (None,math.inf)
            elif winning_move(board,2):
                return (None,-math.inf)
            else: #game over
                return (None,0)
        else: 
          #depth is zero
          return (None,score_position(board,1))
    if player:
        value = -math.inf
        maxcol = random.choice(valid_location)
        for col in valid_location:
            row = get_next(board,col)
            b_copy = board.copy()
            drop(b_copy,row,col,1)
            new_score = minimax(b_copy,depth - 1, False)[1]
            if new_score > value:
                value = new_score
                maxcol = col
        return maxcol, value
    else:
        value = math.inf
        mincol = random.choice(valid_location)
        for col in valid_location:
            row = get_next(board,col)
            b_copy = board.copy()
            drop(b_copy,row,col,2)
            new_score = minimax(b_copy,depth - 1, True)[1]
            if new_score < value:
                value = new_score
                mincol = col
        return mincol, value
        