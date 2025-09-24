import pyautogui


def take_screenshot(step_name):
    screenshot_path = f"reports/screenshots/{step_name}.png"
    pyautogui.screenshot(imageFilename=screenshot_path)

def normalized_name(name):
    return name.replace(" ", "_").lower()