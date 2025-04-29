import gym
import gym_chess
import chess
import random
import sys
import os
from evaluate import evaluate_board
from alphabeta import get_best_move_ab
from utils import save_board_svg_ab

sys.stdout = open('ab_game_log.txt', 'w', encoding='utf-8')

if not os.path.exists("frames_ab"):
    os.makedirs("frames_ab")

env = gym.make('Chess-v0')
state = env.reset()
done = False
move_number = 0
last_white_move = None

print("Initial Board:\n")
print(env.render(mode='unicode'))

while not done:
    board = env._board
    save_board_svg_ab(board, move_number)
    print(env.render(mode='unicode'))

    if board.turn == chess.WHITE:
        move, evaluation, prunes = get_best_move_ab(board, depth=3, last_move=last_white_move)
        last_white_move = move
    else:
        move = random.choice(list(board.legal_moves))
        evaluation = evaluate_board(board)
        prunes = 0

    print(f"\nMove played: {move.uci()}")
    print(f"Evaluation: {evaluation}")
    print("Move by: {'White' if board.turn == chess.WHITE else 'Black'}")
    print(f"Alpha-beta prunes this move: {prunes}")

    state, reward, done, info = env.step(move)
    move_number += 1

save_board_svg_ab(env._board, move_number)
print("\nGame over!")
print(env.render(mode='unicode'))
