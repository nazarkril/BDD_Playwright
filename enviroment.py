from playwright.sync_api import sync_playwright

def before_all(context):
    """Set up Playwright before all tests."""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.browser = browser
    context.playwright = playwright

def before_scenario(context, scenario):
    """Set up a new browser before each scenario."""
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    """Capture a screenshot after each scenario."""
    if scenario.status == "failed":
        screenshot_path = f"reports/screenshots/{scenario.name}.png"
        context.page.screenshot(path=screenshot_path)
    context.page.close()

def after_all(context):
    """Close the browser and stop playwright after all tests."""
    context.browser.close()
    context.playwright.close()
