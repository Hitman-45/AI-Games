import numpy as np
from utils.chess_eval import evaluate

class ChessAlphaBetaAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def act(self, obs, env):
        _, move = self.alphabeta(obs, self.depth, -np.inf, np.inf, True)
        return move

    def alphabeta(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return evaluate(board), None

        legal_moves = list(board.legal_moves)
        best_move = None

        if maximizing:
            max_eval = -np.inf
            for move in legal_moves:
                new_board = board.copy()
                new_board.push(move)
                eval_score, _ = self.alphabeta(new_board, depth - 1, alpha, beta, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = np.inf
            for move in legal_moves:
                new_board = board.copy()
                new_board.push(move)
                eval_score, _ = self.alphabeta(new_board, depth - 1, alpha, beta, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move
