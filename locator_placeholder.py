from playwright.sync_api import expect
def test_get_by_placeholder(page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(10)
    page.get_by_placeholder("Search Amazon.in").fill("mobiles")
    page.wait_for_timeout(10)
    page.keyboard.press("Enter")
    page.wait_for_timeout(10)