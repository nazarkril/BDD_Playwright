import asyncio
import time
from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    print(f"\n▶️ Running scenario: {scenario.name}")


def after_scenario(context, scenario):
    status = scenario.status.name
    print("\n" + "="*60)
    print(f"📘 Scenario: {scenario.name}")
    print(f"📊 Status: {status}")
    print("="*60 + "\n")
    context.page.close()
    context.browser.close()
    context.playwright.stop()