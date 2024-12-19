import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
	print(f' {board[0]} | {board[1]} | {board[2]} ')
	print('-----------')
	print(f' {board[3]} | {board[4]} | {board[5]} ')
	print('-----------')
	print(f' {board[6]} | {board[7]} | {board[8]} ')

def check_winner(board):
	# Check rows
	for i in range(0, 9, 3):
		if board[i] == board[i+1] == board[i+2] and board[i] in ['X', 'O']:
			return board[i]
	# Check columns
	for i in range(3):
		if board[i] == board[i+3] == board[i+6] and board[i] in ['X', 'O']:
			return board[i]
	# Check diagonals
	if board[0] == board[4] == board[8] and board[0] in ['X', 'O']:
		return board[0]
	if board[2] == board[4] == board[6] and board[2] in ['X', 'O']:
		return board[2]
	if all(cell in ['X', 'O'] for cell in board):
		return 'Tie'
	return None

def main():
	board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	player = 'X'

	while True:
		clear_screen()
		print_board(board)
		print(f"Player {player}'s turn")
		
		while True:
			try:
				position = int(input('Enter position (1-9): ')) - 1
				if 0 <= position <= 8 and board[position] not in ['X', 'O']:
					break
				print('Invalid move. Try again.')
			except ValueError:
				print('Please enter a number between 1 and 9.')
		
		board[position] = player
		
		winner = check_winner(board)
		if winner:
			clear_screen()
			print_board(board)
			if winner == 'Tie':
				print('Game Over! It\'s a tie!')
			else:
				print(f'Game Over! Player {winner} wins!')
			break
		
		player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
	main()
