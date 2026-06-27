import keyboard
from PIL import ImageGrab
from pathlib import Path
from datetime import datetime
import tkinter as tk
import threading

# =========================
# Screenshot Settings
# =========================
SAVE_FOLDER = Path.home() / "Pictures" / "Screenshots"
SAVE_FOLDER.mkdir(parents=True, exist_ok=True)

running = True

# =========================
# Screenshot Function
# =========================
def take_screenshot():
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
    filepath = SAVE_FOLDER / filename

    img = ImageGrab.grab(all_screens=True)
    img.save(filepath)

    status.config(text="📸 Screenshot Saved")
    root.after(1500, lambda: status.config(text="🟢 Screenshot Running"))

# =========================
# Exit Function
# =========================
def exit_program():
    global running
    running = False
    keyboard.unhook_all()
    root.destroy()

# =========================
# Keyboard Thread
# =========================
def keyboard_listener():
    keyboard.add_hotkey("F8", take_screenshot)
    keyboard.wait("esc")
    root.after(0, exit_program)

threading.Thread(target=keyboard_listener, daemon=True).start()

# =========================
# Overlay Window
# =========================
root = tk.Tk()

root.title("Screenshot Monitor")
root.geometry("220x70")
root.resizable(False, False)

# Always on top
root.attributes("-topmost", True)

status = tk.Label(
    root,
    text="🟢 Screenshot Running",
    font=("Segoe UI", 11)
)
status.pack(expand=True)

root.protocol("WM_DELETE_WINDOW", exit_program)

root.mainloop()