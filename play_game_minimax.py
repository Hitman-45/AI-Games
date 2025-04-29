import gym
import gym_chess
import chess
import random
import sys
from evaluate import evaluate_board
from minimax import minimax
from utils import save_board_svg

# Log all output
sys.stdout = open('min_max_game_log.txt', 'w', encoding='utf-8')

previous_moves = []

def get_best_move(board, depth):
    best_move = None
    max_eval = float('-inf')
    move_scores = []

    for move in board.legal_moves:
        if len(previous_moves) >= 2 and move == previous_moves[-2]:
            continue

        board.push(move)
        eval = minimax(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()
        move_scores.append((move, eval))

        if eval > max_eval:
            max_eval = eval
            best_move = move

    top_moves = [m for m, e in move_scores if abs(e - max_eval) < 0.2]
    if top_moves:
        best_move = random.choice(top_moves)

    return best_move, max_eval


def play_game(depth=3):
    env = gym.make('Chess-v0')
    state = env.reset()
    done = False
    move_number = 0

    print("Initial Board:\n")
    print(env.render(mode='unicode'))

    while not done:
        board = env._board
        save_board_svg(board, move_number)
        print(env.render(mode='unicode'))

        if board.turn == chess.WHITE:
            move, evaluation = get_best_move(board, depth)
        else:
            move = random.choice(list(board.legal_moves))
            evaluation = evaluate_board(board)

        print(f"\nMove played: {move.uci()}")
        print(f"Evaluation: {evaluation}")
        print("Move by:", "White" if board.turn == chess.WHITE else "Black")

        previous_moves.append(move)
        if len(previous_moves) > 5:
            previous_moves.pop(0)

        state, reward, done, info = env.step(move)
        move_number += 1

    save_board_svg(env._board, move_number)
    print("\nGame over!")
    print(env.render(mode='unicode'))
    print("Result:", env._board.result())
    sys.stdout.close()


if __name__ == "__main__":
    play_game(depth=3)
