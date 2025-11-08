import pyautogui
import pynput.keyboard
import pytesseract

import time

def get_text() -> str:
    screenshot = pyautogui.screenshot(region=(638, 385, 1637 - 638, 554 - 385))
    return pytesseract.image_to_string(
        screenshot, 
        config="tessedit_char_blacklist=|[] tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?.:;"
        )

def main():

    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()

    print("Starting in 5 seconds...")
    time.sleep(3)
    text = get_text().replace("\n", " ").replace("  ", " ")

    mouse.position = (888, 541)
    time.sleep(1)
    mouse.click(pynput.mouse.Button.left)
    time.sleep(1)

    print(repr(text))

    keyboard.type(text)
    

if __name__ == "__main__":
    main()