import chess

def evaluate_board(board):
    if board.is_checkmate():
        return float('-inf') if board.turn == chess.WHITE else float('inf')
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    piece_values = {
        chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3.1,
        chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0
    }

    center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]

    eval = 0
    for piece_type in piece_values:
        eval += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        eval -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]

    # Mobility bonus
    eval += 0.1 * len(list(board.legal_moves)) if board.turn == chess.WHITE else -0.1 * len(list(board.legal_moves))

    # Center control
    for square in center_squares:
        piece = board.piece_at(square)
        if piece:
            eval += 0.2 if piece.color == chess.WHITE else -0.2

    return eval
