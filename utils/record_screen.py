import cv2
import numpy as np
import pyautogui
import time
import os

def record_screen(output_path="videos/game.avi", duration=15, fps=20):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_path, fourcc, fps, screen_size)

    print(f"[REC] Recording screen for {duration} seconds...")
    start_time = time.time()

    while time.time() - start_time < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Correct RGB to BGR
        out.write(frame)
        time.sleep(1 / fps)

    out.release()
    print(f"[✓] Recording saved to {output_path}")
