import time
import os
from datetime import datetime
import pyautogui  # install with: pip install pyautogui

# Ask user for mode
mode = input("Enter mode (full / region): ").strip().lower()

# Ask user for number of screenshots
num = int(input("How many screenshots to take? "))

# Ask user for interval
interval = int(input("Interval (in seconds) between screenshots: "))

# Create folder for screenshots if it doesn’t exist
os.makedirs("screenshots", exist_ok=True)

print("Starting screenshot capture...")

for i in range(num):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/screenshot_{timestamp}.png"
    
    if mode == "region":
        print("Please select the region after 3 seconds...")
        time.sleep(3)
        # Region can be passed as a tuple (x, y, width, height)
        # Example below uses full screen — adjust manually
        screenshot = pyautogui.screenshot(region=(0, 0, 800, 600))
    else:
        screenshot = pyautogui.screenshot()
    
    screenshot.save(filename)
    print(f"Saved {filename}")
    
    if i < num - 1:  # no delay after last one
        time.sleep(interval)

print("\nAll screenshots captured successfully!")
input("Press any key to continue . . . ")
