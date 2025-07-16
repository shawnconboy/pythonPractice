import pyautogui
import time

print("Mouse Mover is running. Press Ctrl+C to stop.")

try:
    while True:
        pyautogui.moveRel(20, 0, duration=0.1)
        pyautogui.moveRel(-20, 0, duration=0.1)
        time.sleep(5)
except KeyboardInterrupt:
    print("\nStopped by user.")
