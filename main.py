import gym
import slimevolleygym
import gym_chess

from agents.minimax_agent import MinimaxAgent
from agents.chess_alphabeta import ChessAlphaBetaAgent
from utils.evaluation import evaluate as slime_evaluate
from utils.chess_eval import evaluate as chess_evaluate
from utils.record_screen import record_screen
import threading
import time


def run_slimevolley_game():
    agent = MinimaxAgent(depth=2)
    env = gym.make("SlimeVolley-v0")
    obs = env.reset()
    done = False
    total_reward = 0

    env.render()  # Launch game window so it's visible
    time.sleep(1)  # Give it a moment to open properly

    # ✅ Start screen recording AFTER window is visible
    recording_thread = threading.Thread(
        target=record_screen,
        args=("videos/slimevolley.avi", 20)
    )
    recording_thread.start()

    while not done:
        action = agent.act(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        env.render()

    try:
        env.close()
    except:
        pass

    print(f"SlimeVolley Minimax Total Reward: {total_reward}")
    recording_thread.join()  # Ensure recording finishes before exit

import threading
from utils.record_screen import record_screen
def run_chess_game():
    # Start screen recording in parallel
    threading.Thread(target=record_screen, args=("videos/chess_game.avi", 15)).start()

    agent = ChessAlphaBetaAgent(depth=2)
    env = gym.make("Chess-v0")
    obs = env.reset()
    done = False

    while not done:
        print(obs)  # Print ASCII board
        action = agent.act(obs, env)
        print(f"Move played: {action}")
        obs, reward, done, _ = env.step(action)

    env.close()
    print(f"Chess AlphaBeta Final Reward: {reward}")

if __name__ == "__main__":
    print("Running Minimax on SlimeVolley...")
    run_slimevolley_game()

    print("Running AlphaBeta on Chess...")
    run_chess_game()