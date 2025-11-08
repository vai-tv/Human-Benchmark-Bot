import pyautogui
import pytesseract

def get_text():
    screenshot = pyautogui.screenshot(region=(1000, 370, 400, 100))
    return pytesseract.image_to_string(screenshot)

FOUND_WORDS = set()

def main():
    for _ in range(350):

        text = get_text().strip()

        if text in FOUND_WORDS:
            # click SEEN
            pyautogui.click(1072, 507)
        else:
            FOUND_WORDS.add(text)
            pyautogui.click(1210, 507)

if __name__ == "__main__":
    main()