import chess
import random
from evaluate import evaluate_board

prune_count = 0

def alphabeta(board, depth, alpha, beta, maximizing_player):
    global prune_count

    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                prune_count += 1
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                prune_count += 1
                break
        return min_eval


def get_best_move_ab(board, depth, last_move=None):
    global prune_count
    prune_count = 0

    best_eval = float('-inf')
    best_moves = []

    legal_moves = list(board.legal_moves)
    random.shuffle(legal_moves)

    for move in legal_moves:
        # Avoid repeating the last move sequence
        if last_move and move.to_square == last_move.from_square and move.from_square == last_move.to_square:
            continue

        board.push(move)
        eval = alphabeta(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()

        if eval > best_eval:
            best_eval = eval
            best_moves = [move]
        elif eval == best_eval:
            best_moves.append(move)

    best_move = random.choice(best_moves) if best_moves else random.choice(legal_moves)
    return best_move, best_eval, prune_count
