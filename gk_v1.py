import keyboard
from PIL import ImageGrab
from datetime import datetime
import os

# Folder to save screenshots
SAVE_FOLDER = "Screenshots"
os.makedirs(SAVE_FOLDER, exist_ok=True)

def take_screenshot():
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
    path = os.path.join(SAVE_FOLDER, filename)

    # Capture all monitors
    img = ImageGrab.grab(all_screens=True)
    img.save(path)

    print(f"Saved: {path}")

# Press F8 to take screenshot
keyboard.add_hotkey("F8", take_screenshot)

print("Running...")
print("Press F8 to take a screenshot.")
print("Press ESC to exit.")

keyboard.wait("esc")