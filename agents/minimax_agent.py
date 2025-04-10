import numpy as np
from utils.evaluation import evaluate

ACTIONS = [
    [0, 0, 0],  # do nothing
    [1, 0, 0],  # left
    [0, 1, 0],  # right
    [0, 0, 1],  # jump
]

class MinimaxAgent:
    def __init__(self, depth=2):
        self.depth = depth

    def act(self, obs):
        _, best_action = self.minimax(obs, self.depth, True)
        return best_action if best_action else [0, 0, 0]

    def minimax(self, obs, depth, maximizing):
        if depth == 0:
            return evaluate(obs), None

        best_action = None
        if maximizing:
            max_eval = -np.inf
            for action in ACTIONS:
                score = evaluate(obs)  # Placeholder for simulation
                if score > max_eval:
                    max_eval = score
                    best_action = action
            return max_eval, best_action
        else:
            min_eval = np.inf
            for action in ACTIONS:
                score = evaluate(obs)
                if score < min_eval:
                    min_eval = score
                    best_action = action
            return min_eval, best_action
