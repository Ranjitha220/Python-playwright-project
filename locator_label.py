from playwright.sync_api import expect
def test_get_by_label(page):
    page.goto("https://demowebshop.tricentis.com/")
    register_link = page.get_by_text("Register")
    register_link.click()
    page.get_by_label("Male").nth(0).check()
    page.get_by_label("First name:").fill("ranju")
    page.get_by_label("Last name:").fill("d")
    page.get_by_label("Email:").fill("ranji@gmail.com")
    page.get_by_label("Password:").nth(0).fill("ranji123")
    page.wait_for_timeout(1000)