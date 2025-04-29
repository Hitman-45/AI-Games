# ♟️ AI Games (Chess Agents)

This project demonstrates the implementation of two classic **adversarial search algorithms** to play the game of Chess using the `gym-chess` environment. It showcases how AI can be used to make optimal decisions in turn-based strategy games by evaluating board states and forecasting opponent responses.

The following algorithms are implemented:

- 🔁 **Minimax** – A brute-force recursive strategy to explore all possible moves and counter-moves up to a fixed depth.
- ✂️ **Alpha-Beta Pruning** – An optimized version of Minimax that prunes branches that cannot affect the final outcome, drastically reducing computation time.

Each algorithm plays against a random opponent, and their behavior is logged, visualized, and converted into videos for analysis. The evaluation function combines material, mobility, and positional heuristics for realistic decision-making.

---

## 📁 Project Structure

*   `AI-Games`
    * `frames_ab/` - Contains frame-by-frame board visualizations for the Alpha-Beta Pruning simulation.
    * `frames_min_max/` - Contains frame-by-frame board visualizations for the Minimax simulation.
    * `videos/` - Contains 3 simulation videos: one for Minimax, one for Alpha-Beta Pruning, and one demonstrating the game execution.
    * `alphabeta.py` - Implements the Alpha-Beta Pruning algorithm with pruning count tracking and move filtering.
    * `evaluate.py` - Contains the evaluation heuristic used by both algorithms (material, mobility, center control, game-over states).
    * `minimax.py` - Implements the standard Minimax algorithm with recursive evaluation.
    * `play_game_ab.py` - Runs a full chess game using Alpha-Beta Pruning as the AI for White, against a random Black opponent.
    * `play_game_minimax.py` - Runs a full chess game using Minimax as the AI for White, against a random Black opponent.
    * `utils.py` - Utility functions for saving board states as SVG frames.
    * `requirements.txt` - Contains all necessary Python dependencies to run the project (gym, gym-chess, python-chess, cairosvg, etc.).
    * `ab_game_log.txt` - Logs of the full Alpha-Beta simulation, including moves, evaluations, and prune counts.
    * `min_max_game_log.txt` - Logs of the full Minimax simulation, including moves and evaluations.
    * `README.md` - Readme file describing project structure, usage, and algorithm information.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Hitman-45/AI-Games.git
cd AI-Games
```

### 2. Setup for the enviroment
```bash
python3 -m venv venv
source venv/bin/activate (for Ubuntu)
venv\Scripts\activate (for Windows)
```

### 3. Install requirements for the algorithms
```bash
pip install -r requirements.txt
```
### 4. Script to run file... 
```bash
python3 play_game_ab.py 
python3 play_game_minimax.py
```