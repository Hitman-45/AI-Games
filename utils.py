import chess
import chess.svg
import os

def save_board_svg(board, move_number):
    if not os.path.exists("frames_min_max"):
        os.makedirs("frames_min_max")
    svg = chess.svg.board(board=board, size=500)
    filepath = f"frames_min_max/board_{move_number:03d}.svg"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)

def save_board_svg_ab(board, move_number):
    svg = chess.svg.board(board=board, size=500)
    filepath = f"frames_ab/board_{move_number:03d}.svg"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
