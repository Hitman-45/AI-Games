def evaluate(board):
    values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0}
    score = 0
    for piece in board.piece_map().values():
        symbol = piece.symbol()
        value = values.get(symbol.upper(), 0)
        score += value if symbol.isupper() else -value

    if board.can_claim_threefold_repetition():
        score -= 0.5  # penalize repetition

    return score
